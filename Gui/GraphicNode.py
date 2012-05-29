# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Simulation.node import Node

import debug

class GraphicNode(QGraphicsObject):

    visibleNodes = 0
    maxVisibleNodes = 50
    index = 0

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

        self.setVisible(False)
        self.setNodeVisible(True)
        self.index = GraphicNode.index
        self.attributes = None

        GraphicNode.index += 1

    def __repr__(self):
        return str(self.index)


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

    def setNodeVisible(self, value):
        if value and not self.isVisible():
            GraphicNode.visibleNodes += 1
        elif not value and self.isVisible():
            GraphicNode.visibleNodes -= 1

        self.setVisible(value)

        if not value:
            for edge in self.outEdges:
                edge.setVisible(False)
            for edge in self.inEdges:
                edge.setVisible(False)
        else:
            for edge in self.outEdges:
                if edge.dest.isVisible():
                    edge.setVisible(True)
            for edge in self.inEdges:
                if edge.source.isVisible():
                    edge.setVisible(True)

        if value:
            self.item.setCheckState(1, Qt.Checked)
        else:
            self.item.setCheckState(1, Qt.Unchecked)

        if value and GraphicNode.visibleNodes > GraphicNode.maxVisibleNodes:
            self.setNodeVisible(False)


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

        if self.attributes.HasAttribute('Color'):
            self.brush.setColor(self.attributes['Color'])
        else:
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
        self.item.setCheckState(1, Qt.Checked)
        self.tree.itemClicked.connect(self.setVisible)

    def setVisible(self, widget, column):
        if widget == self.item and column == 1:
            for node in self.nodes:
                node.setNodeVisible(self.item.checkState(1) == Qt.Checked)

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
