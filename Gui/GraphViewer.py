from Edge import Edge
from Node import Node

__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Gui import Gui
import debug

class GraphViewer(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Gui.Ui_GraphViewer()
        self.ui.setupUi(self)

        self.nodes = []
        self.edges = []

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setAttribute(Qt.WA_Hover)

        self.ui.graphicsView.mouseDoubleClickEvent = self.graphDoubleClick

    @debug.trace()
    def graphDoubleClick(self, event):
        node = self.addNode(event.x(), event.y())

        for n in self.nodes:
            if n != node:
                self.addEdge(n, node)

    @debug.trace()
    def addNode(self, x, y):
        node = Node(self.ui.graphicsView)

        node.setX(x)
        node.setY(y)

        self.nodes.append(node)
        self.scene.addItem(node)

        return node

    @debug.trace()
    def addEdge(self, source, dest):
        edge = Edge(source, dest, self.ui.graphicsView)

        self.edges.append(edge)
        self.scene.addItem(edge)

        return edge

