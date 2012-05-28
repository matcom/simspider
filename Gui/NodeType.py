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

        dlg.ui.cbxIncludeBehavior.setCheckState(Qt.Checked if self.behaviour.includeBehavior else Qt.Unchecked)
        dlg.ui.cbxSendAfterReceive.setCheckState(Qt.Checked if self.behaviour.sendAfterReceive else Qt.Unchecked)

        dlg.setupBehaviours(
            Process=self.behaviour.Process,
            Cleanup=self.behaviour.Cleanup,
            Learn=self.behaviour.Learn,
            OnSignal=self.behaviour.OnSignal,
            Route=self.behaviour.Route,
            Select=self.behaviour.Select,
            Transform=self.behaviour.Transform,
        )

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

            self.behaviour.Process = dlg.behaviours["Process"]
            self.behaviour.Learn = dlg.behaviours["Learn"]
            self.behaviour.Cleanup = dlg.behaviours["Cleanup"]
            self.behaviour.OnSignal = dlg.behaviours["OnSignal"]
            self.behaviour.Route = dlg.behaviours["Route"]
            self.behaviour.Select = dlg.behaviours["Select"]
            self.behaviour.Transform = dlg.behaviours["Transform"]

            self.behaviour.includeBehavior = dlg.ui.cbxIncludeBehavior.checkState() == Qt.Checked
            self.behaviour.sendAfterReceive = dlg.ui.cbxSendAfterReceive.checkState() == Qt.Checked
