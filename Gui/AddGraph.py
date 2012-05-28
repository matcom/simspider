# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui

class AddGraph(QDialog):
    def __init__(self, name, graphViewer):
        QDialog.__init__(self, graphViewer)

        self.ui = ui.Ui_DlgAddGraph()
        self.ui.setupUi(self)

        self.viewer = graphViewer
        self.setWindowTitle("Add Graph; {0}".format(name))


