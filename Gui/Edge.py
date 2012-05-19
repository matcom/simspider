__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

class Edge(QGraphicsItem):

    def __init__(self, sourceNode, destNode, graphics, parent=None):
        QGraphicsItem.__init__(self, parent)

        self.graphics = graphics
        self.source = sourceNode
        self.dest = destNode
        self.adjust()
        self.arrowSize = 5

        self.source.addEdge(self)
        self.dest.addEdge(self)

        self.pen = QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.pen.setWidth(1)

    @debug.trace()
    def adjust(self):
        line = QLineF(self.mapFromItem(self.source, 0, 0), self.mapFromItem(self.dest, 0, 0))
        length = line.length()

        self.prepareGeometryChange()

        if length > 50:
            edgeOffset = QPointF(line.dx() * 15 // length, line.dy() * 15 // length)
            self.sourcePoint = line.p1() + edgeOffset
            self.destPoint = line.p2() - edgeOffset
        else:
            self.sourcePoint = self.destPoint = line.p1()

    def boundingRect(self):
        penWidth = 1
        extra = (penWidth + self.arrowSize) // 2.0

        return QRectF(self.sourcePoint, QSizeF(self.destPoint.x() - self.sourcePoint.x(),
            self.destPoint.y() - self.sourcePoint.y())).\
        normalized().\
        adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, styleoption, widget):
        line = QLineF(self.sourcePoint, self.destPoint)
        painter.setPen(self.pen)
        painter.drawLine(line)
