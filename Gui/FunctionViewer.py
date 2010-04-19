import ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

class FunctionViewer(QDialog):
    def __init__(self, functions, variable):
        QDialog.__init__(self)

        self.functions = functions
        self.variable = variable
        self.ui = ui.Ui_DgFuntions()
        self.ui.setupUi(self)

        for value in self.variable.values:
            self.addValueControl(value)

        self.pages = 0

    def addValueControl(self, value):
        if not self.pages:
            pass





