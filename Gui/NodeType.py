# -*- coding: utf8 -*-
from PyQt4.QtCore import Qt
from EditType import EditType

from Simulation.behavior import Behavior

class NodeType:
    def __init__(self):
        self.behaviour = Behavior()
        self.process = "None"
        self.learn = "None"
        self.route = "None"
        self.select = "None"
        self.transform = "None"
        self.cleanup = "None"
        self.onsignal = "None"

        self.color = Qt.blue
        self.attributes = { }
        self.values = { }
        self.name = "Standard"

    def edit(self):
        dlg = EditType(**self.attributes)
        dlg.ui.lEdName.setText(self.name)

        def setCombo(combo, value):
            combo.setCurrentIndex(combo.findText(value))

        setCombo(dlg.ui.cmbxProcess, self.process)
        setCombo(dlg.ui.cmbxCleanup, self.cleanup)
        setCombo(dlg.ui.cmbxLearn, self.learn)
        setCombo(dlg.ui.cmbxOnSignal, self.onsignal)
        setCombo(dlg.ui.cmbxRoute, self.route)
        setCombo(dlg.ui.cmbxSelect, self.select)
        setCombo(dlg.ui.cmbxTransform, self.transform)

        dlg.color = self.color

        if dlg.exec_():
            self.values = dlg.values()
            self.name = dlg.ui.lEdName.text()

            self.process = dlg.ui.cmbxProcess.currentText()
            self.learn = dlg.ui.cmbxLearn.currentText()
            self.cleanup = dlg.ui.cmbxCleanup.currentText()
            self.onsignal = dlg.ui.cmbxOnSignal.currentText()
            self.route = dlg.ui.cmbxRoute.currentText()
            self.select = dlg.ui.cmbxSelect.currentText()
            self.transform = dlg.ui.cmbxTransform.currentText()
            self.color = dlg.color

            self.attributes = dlg.attributes
            self.action.setText(self.name)
