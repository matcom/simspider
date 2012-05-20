__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Mode:
    def __init__(self, graphics):
        self.graphics = graphics

    def mouseMoveEvent(self, graph, event):
        pass

    def mouseClickEvent(self, graph, event):
        pass

    def mouseDoubleClickEvent(self, graph, event):
        pass


class SelectionMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.RubberBandDrag)


class MoveMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.ScrollHandDrag)

    def mouseDoubleClickEvent(self, graph, event):
        self.graphics.centerOn(self.graphics.mapToScene(event.pos()))


class CreationMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)

    def mouseDoubleClickEvent(self, graph, event):
        graph.addNode(self.graphics.mapToScene(event.pos()))


class CliqueMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mouseDoubleClickEvent(self, graph, event):
        node = graph.addNode(self.graphics.mapToScene(event.pos()))

        for x in self.nodes:
            graph.addEdge(node, x)
            graph.addEdge(x, node)

        self.nodes.append(node)


class CycleMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mouseDoubleClickEvent(self, graph, event):
        node = graph.addNode(self.graphics.mapToScene(event.pos()))

        if len(self.nodes) > 1:
            graph.removeEdge(self.nodes[-1], self.nodes[0])

        if len(self.nodes) > 0:
            graph.addEdge(self.nodes[-1], node)
            graph.addEdge(node, self.nodes[0])

        self.nodes.append(node)


class PathMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mouseDoubleClickEvent(self, graph, event):
        node = graph.addNode(self.graphics.mapToScene(event.pos()))

        if len(self.nodes) > 0:
            graph.addEdge(self.nodes[-1], node)

        self.nodes.append(node)
