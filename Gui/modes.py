# -*- coding: utf8 -*-

from GraphicEdge import GraphicEdge
from GraphicNode import GraphicNode, Subgraph

import debug

__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Mode:
    def __init__(self, graphics):
        self.graphics = graphics
        self.translating = False

    def mouseWheel(self, graph, event):
        s = event.delta() / 120.0 * 0.9
        if s < 0:
            s = 1/-s
        print(s)
        self.graphics.scale(s, s)

        return True

    def mouseMoveEvent(self, graph, event):
        if self.translating:
            self.graphics.translate(event.x() - self.x, event.y() - self.y)
            debug.debug("Translating by ({0},{1})", (event.x() - self.x, event.y() - self.y), "gui")
            self.x = event.x()
            self.y = event.y()

            return True

        return False

    def mouseDoubleClickEvent(self, graph, event):
        return False

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.MiddleButton:
            self.x = event.x()
            self.y = event.y()
            debug.debug("Beginning translation on ({0},{1})", (self.x, self.y), "gui")
            self.translating = True

            return True

        return False

    def mouseReleaseEvent(self, graph, event):
        if event.button() == Qt.MiddleButton:
            debug.debug("Ending translation on ({0},{1})", (self.x, self.y), "gui")
            self.translating = False

            return True

        return False

class SelectionMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.RubberBandDrag)
        self.clicked = None

    def mouseDoubleClickEvent(self, graph, event):
        nodes = graph.selectedNodes()
        items = []

        for x in nodes:
            items += x.walk()

        items = set(items)

        if not items:
            items = graph.nodes

        graph.deselectAll()

        for x in items:
            x.setSelected(True)

        self.clicked = True
        return True

    def mouseReleaseEvent(self, graph, event):
        done = False

        if super().mouseReleaseEvent(graph, event):
            return True

        if self.clicked:
            done = True
            self.clicked = False

        return done


class ConnectMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.selected = None
        self.edge = None
        self.node = GraphicNode(graphics)

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            nodes = graph.nodesAt(event.x(), event.y())
            graph.deselectAll()

            if self.edge:
                self.graphics.scene().removeItem(self.edge)
                self.edge = None

            if not nodes:
                self.selected = None
                return False

            self.selected = nodes[0]
            self.node.setPos(self.selected.pos())
            self.edge = GraphicEdge(self.selected, self.node, self.graphics)
            self.graphics.scene().addItem(self.edge)
            self.edge.adjust()
            self.selected.setSelected(True)

        elif super().mousePressEvent(graph, event):
            return True

        return True

    def mouseReleaseEvent(self, graph, event):
        if super().mouseReleaseEvent(graph, event):
            return True

        if event.button() == Qt.LeftButton:
            nodes = graph.nodesAt(event.x(), event.y())

            if self.edge:
                self.graphics.scene().removeItem(self.edge)
                self.edge = None

            if not nodes or not self.selected:
                if self.selected:
                    self.selected.setSelected(False)
                return False

            node = nodes[0]
            graph.addEdge(self.selected, node)

        return True

    def mouseMoveEvent(self, graph, event):
        if self.edge:

            if not self.node:
                debug.error("No node !!!", Exception(), "modes.connect")
                return False

            self.node.setPos(self.graphics.mapToScene(event.pos()))
            self.edge.adjust()
            debug.info("Moving edge {0}", (self.edge,), "modes.connect")

        elif super().mouseMoveEvent(graph, event):
            return True

        return True


class CreationMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            node = graph.addNode(self.graphics.mapToScene(event.pos()))
            edges = graph.edgesAt(event.x(), event.y())

            for e in edges:
                graph.insertNode(node, e)

        elif super().mousePressEvent(graph, event):
            return True

        return False


class CliqueMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            if not self.nodes:
                self.subgraph = Subgraph("Clique", graph)

            node = graph.addNode(self.graphics.mapToScene(event.pos()), self.subgraph)

            for x in self.nodes:
                graph.addEdge(node, x)
                graph.addEdge(x, node)

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        elif super().mousePressEvent(graph, event):
            return True

        return False


class CycleMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            if not self.nodes:
                self.subgraph = Subgraph("Cycle", graph)

            node = graph.addNode(self.graphics.mapToScene(event.pos()), self.subgraph)

            if len(self.nodes) > 1:
                graph.removeEdge(self.nodes[-1], self.nodes[0])

            if len(self.nodes) > 0:
                graph.addEdge(self.nodes[-1], node)
                graph.addEdge(node, self.nodes[0])

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        elif super().mousePressEvent(graph, event):
            return True

        return False


class PathMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button == Qt.LeftButton:
            if not self.nodes:
                self.subgraph = Subgraph("Path", graph)

            node = graph.addNode(self.graphics.mapToScene(event.pos()), self.subgraph)

            if len(self.nodes) > 0:
                graph.addEdge(self.nodes[-1], node)

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        elif super().mousePressEvent(graph, event):
            return True

        return False
