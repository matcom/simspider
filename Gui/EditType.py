# -*- coding: utf8 -*-
from PropertyViewer import *
import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
from Plugins import pluginManager

class EditType(QDialog):

    table = { ord(l) : " " + l for l in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") }

    types = { item.__name__ : item for item in [Integer, Float, String, Bool]}

    def __init__(self, title="Edit Type", icon=None, **kwargs):
        QDialog.__init__(self)

        self.attributes = kwargs
        self.ui = ui.Ui_DgEditType()

        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle(title)

        self.combos = {
            "Process" : self.ui.cmbxProcess,
            "Cleanup" : self.ui.cmbxCleanup,
            "Learn" : self.ui.cmbxLearn,
            "OnSignal" : self.ui.cmbxOnSignal,
            "Route" : self.ui.cmbxRoute,
            "Select" : self.ui.cmbxSelect,
            "Transform" : self.ui.cmbxTransform,
            }

        layout = self.ui.formLayout

        for name, type in self.attributes.items():
            type.build(name.translate(EditType.table), layout, QCheckBox)

        self._setupBehaviours()
        self.color = Qt.blue

        self.ui.btnAdd.clicked.connect(self.addAttribute)
        self.ui.btnRemove.clicked.connect(self.removeAttributes)

        self.ui.btnColor.clicked.connect(self.setColor)

    def setColor(self):
        self.color = QColorDialog.getColor(self.color, self)

    def addAttribute(self):
        name, ok = QInputDialog.getText(self, "Add new attribute", "Enter the attribute name")

        if not ok:
            return

        text, ok = QInputDialog.getItem(self, "Add new attribute", "Select the attribute type",
                                        list(self.types.keys()))
        if not ok:
            return

        type = self.types[text]()
        self.attributes[name] = type
        type.build(name, self.ui.formLayout, QCheckBox)

    def removeAttributes(self):
        pass

    def values(self):
        values = {}

        for name, item in self.attributes.items():
            values[name] = item.value()

        return values

    def setValues(self, **kwargs):
        for name, item in kwargs.items():
            self.attributes[name].setValue(item)

    def _setupBehaviours(self):
        for name, combo in self.combos.items():
            self._setupBehaviour(name, combo)

    def setupBehaviours(self, **behaviours):
        self.behaviours = behaviours

        for name, combo in self.combos.items():
            self._setupCombo(name, combo)

    def _setupCombo(self, name, combo):
        def setup(index):
            if not index:
                self.behaviours[name] = None
            else:
                self.behaviours[name] = combo.itemData(index).setup()

        combo.currentIndexChanged.connect(setup)

    def _setupBehaviour(self, name, combo):
        items = pluginManager.getItems("Behaviour.{0}".format(name))

        for item in items:
            combo.addItem(item.name, item)

