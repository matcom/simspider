# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
import math

class GraphicFun(QGraphicsItem):

    def __init__(self, function, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.function = function

        self.pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(Qt.black)


    def shape(self):
        return QRectF(0,0,100,100)

    def boundingRect(self):
        return QRectF(0,0,100,100)

    def paint(self, painter, styleoption, widget):

        points = self.function.evaluate(100)
        painter.setPen(self.pen)

        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            p1 = QPointF(x1, -y1 * 100)
            p2 = QPointF(x2, -y2* 100)
            line = QLineF(p1, p2)
            painter.drawLine(line)


class FuncAxis(QGraphicsItem):
    def __init__(self, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics

        self.pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(Qt.black)

    def shape(self):
        return QRectF(0,0,100,100)

    def boundingRect(self):
        return self.shape()

    def paint(self, painter, styleoption, widget):
        painter.setPen(self.pen)

        p00 = QPointF(0,0)
        p01 = QPointF(0,-100)
        p10 = QPointF(100,0)

        line01 = QLineF(p00, p01)
        line10 = QLineF(p00, p10)

        painter.drawLine(line01)
        painter.drawLine(line10)
