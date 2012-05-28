from Code import CodeDialog
import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

class PropertyViewer(QDialog):

    table = { ord(l) : " " + l for l in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") }

    def __init__(self, title="Property Viewer", icon=None, **kwargs):
        QDialog.__init__(self)

        self.kwargs = kwargs
        self.ui = ui.Ui_PropertyViewer()

        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle(title)

        layout = QFormLayout()

        for name, type in self.kwargs.items():
            type.build(name.translate(PropertyViewer.table), layout)

        self.ui.scrollArea.setLayout(layout)

    @debug.trace()
    def values(self):
        values = {}

        for name, item in self.kwargs.items():
            values[name] = item.value()

        return values

    def setValues(self, **kwargs):
        for name, item in kwargs.items():
            self.kwargs[name].setValue(item)


class Property:

    @debug.trace()
    def build(self, name, layout, label=QLabel):
        self.name = name
        self.layout = layout
        self.item = self._getItem()
        self.layout.addRow(label(self.name), self.item)

    def value(self):
        pass

    def setValue(self, value):
        pass

    def _getItem(self):
        pass


class Integer(Property):
    def __init__(self, value=0, min=0 , max=100, step=1):
        self.min = min
        self.max = max
        self.val = value
        self.step = step

    @debug.trace()
    def _getItem(self):
        item = QSpinBox()
        item.setValue(self.val)
        item.setMinimum(self.min)
        item.setMaximum(self.max)
        item.setSingleStep(self.step)

        return item

    @debug.trace()
    def value(self):
        return self.item.value()

    def setValue(self, value):
        self.item.setValue(value)


class Float(Property):
    def __init__(self, value=0.0, min=0.0, max=1.0, step=0.01):
        self.min = min
        self.max = max
        self.val = value
        self.step = step

    @debug.trace()
    def _getItem(self):
        item = QDoubleSpinBox()
        item.setValue(self.val)
        item.setMinimum(self.min)
        item.setMaximum(self.max)
        item.setSingleStep(self.step)

        return item

    @debug.trace()
    def value(self):
        return self.item.value()

    def setValue(self, value):
        self.item.setValue(value)


class Bool(Property):
    def __init__(self, value=False):
        self.val = value

    @debug.trace()
    def _getItem(self):
        item = QCheckBox()
        item.setChecked(self.val)

        return item

    @debug.trace()
    def value(self):
        return self.item.checkState() == Qt.Checked

    def setValue(self, value):
        self.item.setCheckState(Qt.Checked if value else Qt.Unchecked)


class String(Property):
    def __init__(self, value=""):
        self.val = value

    @debug.trace()
    def _getItem(self):
        item = QLineEdit()
        item.setText(self.val)

        return item

    @debug.trace()
    def value(self):
        return self.item.text()

    def setValue(self, value):
        self.item.setText(value)


class Option(Property):
    def __init__(self, values=("None",)):
        self.values = values
        self.index = 0

    @debug.trace()
    def _getItem(self):
        item = QComboBox()
        item.addItems(self.values)
        item.setCurrentIndex(0)

        return item

    @debug.trace()
    def value(self):
        return self.item.currentIndex()

    def setValue(self, value):
        self.item.setCurrentIndex(value)


class Code(Property):
    def __init__(self, functionName, functionArgs=(), globalArgs=None):
        self.functionName = functionName
        self.functionArgs = functionArgs
        self.globalArgs = globalArgs

    @debug.trace()
    def _getItem(self):
        item = QPushButton()
        item.setText("Enter Code Snippet")
        item.clicked.connect(self._itemClicked(item))

        return item

    def _itemClicked(self, item):
        def clicked():
            item.code = CodeDialog(self.functionName, self.functionArgs, self.globalArgs)

            if item.code.exec_():
                item.method = item.code.compile()
            else:
                item.method = None
        return clicked

    @debug.trace()
    def value(self):
        return self.item.method

    def setValue(self, value):
        pass
