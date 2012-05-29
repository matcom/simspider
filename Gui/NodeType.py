# -*- coding: utf8 -*-
from PyQt4.QtCore import Qt
from EditType import EditType

from Simulation.behavior import Behavior
from Simulation.node import NodePrototype

class NodeType:
    def __init__(self, graph):
        self.process = "None"
        self.learn = "None"
        self.route = "None"
        self.select = "None"
        self.transform = "None"
        self.cleanup = "None"
        self.onsignal = "None"

        self.nodes = set()
        self.graph = graph

        self.prototype = NodePrototype()

        self.color = Qt.blue
        self.attributes = { }
        self.name = "Standard"

    def apply(self):
        self.prototype.ApplyTo(self.nodes, self.graph)

        for n in self.nodes:
            if n.isVisible():
                n.update()

    def add(self, node):
        if not node in self.nodes:
            self.nodes.add(node)

    def remove(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

    def edit(self):
        dlg = EditType(**self.attributes)
        dlg.ui.lEdName.setText(self.name)
        b = self.prototype.GetBehavior()

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

        dlg.ui.cbxIncludeBehavior.setCheckState(Qt.Checked if b.includeBehavior else Qt.Unchecked)
        dlg.ui.cbxSendAfterReceive.setCheckState(Qt.Checked if b.sendAfterReceive else Qt.Unchecked)

        dlg.setupBehaviours(
            Process=b.Process,
            Cleanup=b.Cleanup,
            Learn=b.Learn,
            OnSignal=b.OnSignal,
            Route=b.Route,
            Select=b.Select,
            Transform=b.Transform,
        )

        if dlg.exec_():
            self.name = dlg.ui.lEdName.text()
            b.name = self.name
            self.prototype.DefineAttributes(dlg.values())
            self.prototype.DefineAttribute("Color", self.color)

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

            b.Process = dlg.behaviours["Process"]
            b.Learn = dlg.behaviours["Learn"]
            b.Cleanup = dlg.behaviours["Cleanup"]
            b.OnSignal = dlg.behaviours["OnSignal"]
            b.Route = dlg.behaviours["Route"]
            b.Select = dlg.behaviours["Select"]
            b.Transform = dlg.behaviours["Transform"]

            # TODO: Si le pongo None a un behaviour, explota

            b.includeBehavior = dlg.ui.cbxIncludeBehavior.checkState() == Qt.Checked
            b.sendAfterReceive = dlg.ui.cbxSendAfterReceive.checkState() == Qt.Checked

            self.apply()
