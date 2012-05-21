# -*- coding: utf8 -*-

__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug
import math

class GraphicEdge(QGraphicsItem):

    def __init__(self, sourceNode, destNode, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.source = sourceNode
        self.dest = destNode
        self.adjust()
        self.arrowSize = 10

        self.source.addOutEdge(self)
        self.dest.addInEdge(self)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        self.pen = QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(Qt.black)

    @debug.trace()
    def adjust(self):
        line = QLineF(self.mapFromItem(self.source, 0, 0), self.mapFromItem(self.dest, 0, 0))
        length = line.length()

        self.prepareGeometryChange()

        if length > 25:
            edgeOffset = QPointF(line.dx() * 15 // length, line.dy() * 15 // length)
            self.sourcePoint = line.p1() + edgeOffset
            self.destPoint = line.p2() - edgeOffset
        else:
            self.sourcePoint = self.destPoint = line.p1()

    def shape(self):
        stroker = QPainterPathStroker()
        path = QPainterPath(self.sourcePoint)
        path.lineTo(self.destPoint)

        stroker.setWidth(10)
        return stroker.createStroke(path)

    def boundingRect(self):
        penWidth = 1
        extra = (penWidth + self.arrowSize) // 2.0

        return QRectF(self.sourcePoint, QSizeF(self.destPoint.x() - self.sourcePoint.x(),
            self.destPoint.y() - self.sourcePoint.y())).\
        normalized().\
        adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, styleoption, widget):

        if self.isSelected():
            self.pen.setColor(Qt.red)
            self.brush.setColor(Qt.red)
        else:
            self.pen.setColor(Qt.black)
            self.brush.setColor(Qt.black)

        line = QLineF(self.sourcePoint, self.destPoint)
        painter.setPen(self.pen)
        painter.drawLine(line)

        if line.length() <= self.arrowSize:
            return

        angle = math.acos(line.dx() / line.length())

        if line.dy() >= 0:
            angle = 2 * math.pi - angle

        sourceArrowP1 = self.destPoint + QPointF(math.sin(angle - math.pi // 3) * self.arrowSize,
            math.cos(angle - math.pi // 3) * self.arrowSize)

        sourceArrowP2 = self.destPoint + QPointF(math.sin(angle - math.pi + math.pi // 3) * self.arrowSize,
            math.cos(angle - math.pi + math.pi // 3) * self.arrowSize)

        painter.setBrush(self.brush)
        painter.drawPolygon(QPolygonF([line.p2(), sourceArrowP1, sourceArrowP2]))
