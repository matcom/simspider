# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import debug

class GraphicNode(QGraphicsObject):

    def __init__(self, graphics, parent=None):
        QGraphicsObject.__init__(self, parent)

        self.graphics = graphics
        self.circle = QPainterPath()
        self.circle.addEllipse(-15,-15,30,30)
        self.pen = QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.brush = QBrush(QColor(0,0,255,255))

        self.outEdges = []
        self.inEdges = []

        self.isBipartite = False

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)

        self.item = QTreeWidgetItem(["Node"], 0)
        self.item.node = self
        self.subgraph = None

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

    def walk(self):
        items = set()
        self._walk(items)
        return items

    def all(self):
        items = set()
        self._all(items)
        return items

    def _all(self, items):
        if not self in items:
            items.add(self)
            for e in self.outEdges:
                e.dest._all(items)
            for e in self.inEdges:
                e.source._all(items)

    def _walk(self, items):
        if not self in items:
            items.add(self)
            for e in self.outEdges:
                e.dest._walk(items)

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
            self.pen.setColor(QColor(255,0,0))
        elif self.isBipartite:
            self.pen.setColor(QColor(0,255,0))
        else:
            self.pen.setColor(QColor(0,0,0))

        self.brush.setColor(self.nodeType.color)

        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPath(self.circle)

    def connect(self, parent):
        if self.subgraph:
            self.disconnect()

        self.subgraph = parent
        parent.addNode(self)
        self.update()

    def disconnect(self):
        self.subgraph.removeNode(self)
        self.subgraph = None

    def update(self):
        self.item.setText(0, "Node")


class Subgraph:
    def __init__(self, name, graph):
        self.graph = graph
        self.name = name
        self.nodes = []
        self.tree = graph.ui.graphTree
        self.item = QTreeWidgetItem([name], 0)

        self.tree.addTopLevelItem(self.item)
        self.update()

    def addNode(self, node):
        self.nodes.append(node)
        self.item.addChild(node.item)
        self.item.setSelected(True)
        self.item.setExpanded(True)
        self.update()

    def removeNode(self, node):
        self.nodes.remove(node)
        index = self.item.indexOfChild(node.item)
        self.item.takeChild(index)
        self.update()

    def delete(self):
        index = self.tree.indexOfTopLevelItem(self.item)
        self.tree.takeTopLevelItem(index)

    def update(self):
        self.item.setText(0, "{0} ({1} items)".format(self.name, len(self.nodes)))
