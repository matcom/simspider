# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

__author__ = 'Alejandro Piad'

class GraphicNode(QGraphicsItem):

    def __init__(self, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.circle = QPainterPath()
        self.circle.addEllipse(-15,-15,30,30)
        self.pen = QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(QColor(0,0,255,128))

        self.outEdges = []
        self.inEdges = []

        self.isBipartite = False

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

    @debug.trace()
    def addInEdge(self, edge):
        self.inEdges.append(edge)

    def addOutEdge(self, edge):
        self.outEdges.append(edge)

    def removeEdge(self, edge):
        if edge in self.inEdges:
            self.inEdges.remove(edge)

        if edge in self.outEdges:
            self.outEdges.remove(edge)

    def shape(self):
        return self.circle

    def boundingRect(self):
        return self.circle.boundingRect().adjusted(-1,-1,1,1)

    @debug.trace()
    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self.inEdges + self.outEdges:
                edge.adjust()

        return QGraphicsItem.itemChange(self, change, value)


    def paint(self, painter, styleoption, widget):
        if self.isSelected():
            self.brush.setColor(QColor(255,0,0,128))
        elif self.isBipartite:
            self.brush.setColor(QColor(0,255,0,128))
        else:
            self.brush.setColor(QColor(0,0,255,128))

        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPath(self.circle)

    def __repr__(self):
        return "GraphicNode(X = {0}, Y = {1})".format(self.x(), self.y())
