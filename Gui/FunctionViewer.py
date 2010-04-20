import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug


class Variable:
    def __init__(self, name):
        self.name = name
        self.values = {}


class Function:
    def __init__(self, name, **kwargs):
        self.name = name
        self.properties = kwargs

    def clone(self):
        return Function(self.name, **self.properties)


class FunctionViewer(QDialog):
    def __init__(self, functions, variable):
        QDialog.__init__(self)

        self.functions = functions
        self.variable = variable
        self.functionNames = list(self.functions.keys())

        self.ui = ui.Ui_DgFuntions()
        self.ui.setupUi(self)

        self.pages = 0

        self.ui.toolBox.setVisible(False)

        for name, func in self.variable.values.items():
            self.addValueControl(name, func)

        self.ui.btnAdd.clicked.connect(self.addValue)
        self.ui.btnRemove.clicked.connect(self.removeValue)


    def addValue(self):
        text, ok = QInputDialog.getText(self, "Add a new value", "Name")

        if not ok:
            return

        self.variable.values[text] = Function("None")
        self.addValueControl(text, Function("None"))


    def removeValue(self):
        page = self.ui.toolBox.currentWidget()
        text = self.ui.toolBox.itemText(self.ui.toolBox.currentIndex())

        if self.pages > 1:
            self.ui.toolBox.removeItem(self.ui.toolBox.currentIndex())
            page.deleteLater()

        self.pages -= 1

        self.variable.values.pop(text)

        if not self.pages:
            self.ui.btnRemove.setEnabled(False)
            self.ui.toolBox.setVisible(False)


    def addValueControl(self, name, func):
        if not self.pages:
            self.ui.toolBox.setVisible(True)
            self.ui.btnRemove.setEnabled(True)

            page = self.ui.toolBox.widget(0)
            self.ui.toolBox.setItemText(0, name)
            layout = page.layout()

            if layout:
                layout.deleteLater()

        else:
            page = QWidget()
            self.ui.toolBox.addItem(page, name)

        layout = QFormLayout()
        page.setLayout(layout)

        combo = QComboBox()
        combo.addItems(self.functionNames)

        for i,s in enumerate(self.functionNames):
            if s == func.name:
                combo.setCurrentIndex(i)
                break

        layout.addRow("Type", combo)

        def setupItem():
            func = self.functions[combo.currentText()].clone()

            while layout.count() > 2:
                item = layout.takeAt(2)
                item.widget().deleteLater()

            for name, value in func.properties.items():
                spin = QDoubleSpinBox()

                spin.setMinimum(-1000)
                spin.setMaximum(1000)
                spin.setValue(value)
                layout.addRow(name, spin)

        combo.currentIndexChanged.connect(setupItem)
        setupItem()

        self.pages += 1
