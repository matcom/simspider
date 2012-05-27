# -*- coding: utf8 -*-

from PropertyViewer import *
import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
from Plugins import pluginManager

class EditType(QDialog):

    table = { ord(l) : " " + l for l in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") }

    def __init__(self, title="Edit Type", icon=None, **kwargs):
        QDialog.__init__(self)

        self.kwargs = kwargs
        self.ui = ui.Ui_DgEditType()

        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle(title)

        layout = self.ui.formLayout

        for name, type in self.kwargs.items():
            type.build(name.translate(EditType.table), layout, QCheckBox)

        self._setupBehaviours()

    def values(self):
        values = {}

        for name, item in self.kwargs.items():
            values[name] = item.value()

        return values

    def setValues(self, **kwargs):
        for name, item in kwargs.items():
            self.kwargs[name].setValue(item)

    def _setupBehaviours(self):
        combos = {
            "Process" : self.ui.cmbxProcess,
            "Cleanup" : self.ui.cmbxCleanup,
            "Learn" : self.ui.cmbxLearn,
            "OnSignal" : self.ui.cmbxOnSignal,
            "Route" : self.ui.cmbxRoute,
            "Select" : self.ui.cmbxSelect,
            "Transform" : self.ui.cmbxTransform,
        }

        for name, combo in combos.items():
            self._setupBehaviour(name, combo)

    def _setupBehaviour(self, name, combo):
        items = pluginManager.getItems("Behaviour.{0}".format(name))

        for item in items:
            combo.addItem(item.name, item)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    dlg = EditType(Age=Integer(), Value=Float(), IsGay=Bool(), SomeString=String())
    dlg.exec_()

    print(dlg.values())



