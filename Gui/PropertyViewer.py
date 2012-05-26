import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

class PropertyViewer(QDialog):
    def __init__(self, title="Property Viewer", icon=None, **kwargs):
        QDialog.__init__(self)

        self.kwargs = kwargs
        self.ui = ui.Ui_PropertyViewer()

        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle(title)

        layout = QFormLayout()

        for name, type in self.kwargs.items():
            type.build(name, layout)

        self.ui.scrollArea.setLayout(layout)

    @debug.trace()
    def values(self):
        values = {}

        for name, item in self.kwargs.items():
            values[name] = item.value()

        return values


class PropertyBuilder:

    @debug.trace()
    def build(self, name, layout):
        self.name = name
        self.layout = layout
        self.item = self._getItem()
        self.layout.addRow(name, self.item)

    def value(self):
        pass

    def _getItem(self):
        pass


class IntegerBuilder(PropertyBuilder):
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


class FloatBuilder(PropertyBuilder):
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
