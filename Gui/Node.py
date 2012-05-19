from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

__author__ = 'Alejandro Piad'

class Node(QGraphicsItem):

    def __init__(self, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.circle = QPainterPath()
        self.circle.addEllipse(-15,-15,30,30)
        self.pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(QColor(0,0,255,128))

        self.edges = []

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    @debug.trace()
    def addEdge(self, edge):
        self.edges.append(edge)

    def shape(self):
        return self.circle

    def boundingRect(self):
        return self.circle.boundingRect().adjusted(-1,-1,1,1)

    @debug.trace()
    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.edges:
                edge.adjust()

        return QGraphicsItem.itemChange(self, change, value)


    def paint(self, painter, styleoption, widget):
        if self.isSelected():
            self.brush.setColor(QColor(255,0,0,128))
        elif self.isUnderMouse():
            self.brush.setColor(QColor(0,0,255,255))
        else:
            self.brush.setColor(QColor(0,0,255,128))

        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPath(self.circle)

    def __repr__(self):
        return "Node(X = {0}, Y = {1})".format(self.x(), self.y())
