__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Mode:
    def __init__(self, graphics):
        self.graphics = graphics

    def mouseMoveEvent(self, graph, event):
        return False

    def mouseDoubleClickEvent(self, graph, event):
        return False

    def mousePressEvent(self, graph, event):
        return False

    def mouseReleaseEvent(self, graph, event):
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

        if self.clicked:
            done = True
            self.clicked = False

        return done


class ConnectMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.ScrollHandDrag)

    def mouseDoubleClickEvent(self, graph, event):
        self.graphics.centerOn(self.graphics.mapToScene(event.pos()))

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

        return False


class CliqueMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            node = graph.addNode(self.graphics.mapToScene(event.pos()))

            for x in self.nodes:
                graph.addEdge(node, x)
                graph.addEdge(x, node)

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        return False


class CycleMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button() == Qt.LeftButton:
            node = graph.addNode(self.graphics.mapToScene(event.pos()))

            if len(self.nodes) > 1:
                graph.removeEdge(self.nodes[-1], self.nodes[0])

            if len(self.nodes) > 0:
                graph.addEdge(self.nodes[-1], node)
                graph.addEdge(node, self.nodes[0])

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        return False


class PathMode(Mode):
    def __init__(self, graphics):
        Mode.__init__(self, graphics)
        self.graphics.setDragMode(QGraphicsView.NoDrag)
        self.nodes = []

    def mousePressEvent(self, graph, event):
        if event.button == Qt.LeftButton:
            node = graph.addNode(self.graphics.mapToScene(event.pos()))

            if len(self.nodes) > 0:
                graph.addEdge(self.nodes[-1], node)

            self.nodes.append(node)

        elif event.button() == Qt.RightButton:
            self.nodes = []
            graph.deselectAll()

        return False
