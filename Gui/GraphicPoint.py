# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
import math

class GraphicPoint(QGraphicsItem):

    def __init__(self, function, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.function = function

        self.pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(Qt.black)


    def shape(self):
        return QRect(-5,-5,5,5)

    def boundingRect(self):
        return QRect(-5,-5,5,5)

    @debug.trace()
    def paint(self, painter, styleoption, widget):
        painter.drawEllipse(self.shape())
