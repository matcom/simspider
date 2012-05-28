# -*- coding: utf8 -*-
from GraphicFun import GraphicFun, FuncAxis
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

    def __getattr__(self, item):
        return self.properties[item]

    def evaluate(self, precision):
        pass


class TriangularFunction(Function):
    def __init__(self, min=0, mid=50, max=100):
        Function.__init__(self, "Triangular", Min=min, Mid=mid, Max=max)

    def clone(self):
        return TriangularFunction(self.Min, self.Mid, self.Max)

    def evaluate(self, precision):
        return [(self.Min,0), (self.Mid, 1), (self.Max, 0)]


class SquareFunction(Function):
    def __init__(self, min=0, max=100):
        Function.__init__(self, "Square", Min=min, Max=max)

    def clone(self):
        return SquareFunction(self.Min, self.Max)

    def evaluate(self, precision):
        return [(self.Min,0), (self.Min, 1), (self.Max, 1), (self.Max, 0)]


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

        self.ui.btnAdd.clicked.connect(self.addValue)
        self.ui.btnRemove.clicked.connect(self.removeValue)

        self.scene = QGraphicsScene()
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)

        self.ui.functionView.setScene(self.scene)
        self.ui.functionView.setAttribute(Qt.WA_Hover)
        self.axis = FuncAxis(self.ui.functionView)
        self.scene.addItem(self.axis)
        self.scene.setSceneRect(-5,-5,110,110)

        for name, func in self.variable.values.items():
            self.addValueControl(name, func)

    #Agrega un valor linguístico
    def addValue(self):
        text, ok = QInputDialog.getText(self, "Add a new value", "Name")

        if not ok:
            return

        self.variable.values[text] = Function("None")
        self.addValueControl(text, Function("None"))

    #Elimina un valor linguístico
    def removeValue(self):
        page = self.ui.toolBox.currentWidget()
        text = self.ui.toolBox.itemText(self.ui.toolBox.currentIndex())

        if self.pages > 1:
            self.ui.toolBox.removeItem(self.ui.toolBox.currentIndex())

            if hasattr(page, "function") and page.function:
                self.scene.removeItem(page.function)

            page.deleteLater()

        self.pages -= 1

        self.variable.values.pop(text)

        if not self.pages:
            self.ui.btnRemove.setEnabled(False)
            self.ui.toolBox.setVisible(False)

        self.scene.update()

    #Agrega para un valor linguístico agrega todos los controles.
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

            if hasattr(page, "function") and page.function:
                self.scene.removeItem(page.function)

            page.function = GraphicFun(func, self.ui.functionView)
            self.scene.addItem(page.function)

            while layout.count() > 2:
                item = layout.takeAt(2)
                item.widget().deleteLater()

            for name, value in func.properties.items():
                spin = QDoubleSpinBox()

                spin.setMinimum(-1000)
                spin.setMaximum(1000)
                spin.setValue(value)
                layout.addRow(name, spin)

                spin.valueChanged.connect(self.connectValueChanged(func, name))

            self.scene.update()

        combo.currentIndexChanged.connect(setupItem)
        setupItem()

        self.pages += 1

    def connectValueChanged(self, func, name):
        def valueChanged(value):
            func.properties[name] = value
            self.scene.update()

        return valueChanged

