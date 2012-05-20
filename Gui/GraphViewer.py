# -*- coding: utf8 -*-
import math

from GraphicEdge import GraphicEdge
from GraphicNode import GraphicNode

from builders import *
from modes import *

__author__ = 'Alejandro Piad'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui
import debug

import networkx as nx

from Plugins import pluginManager

class GraphViewer(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = ui.Ui_GraphViewer()
        self.ui.setupUi(self)

        self.nodes = []     # Almacena los nodos
        self.edges = []     # Almacena las aristas
        self.edgesDict = {} # Permite acceder rápidamente a las aristas por (source, dest)

        self.scene = QGraphicsScene()
        self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setAttribute(Qt.WA_Hover)

        self.ui.graphicsView.mouseDoubleClickEvent = self.graphDoubleClick
        # self.ui.graphicsView.wheelEvent = self.graphWheel

        self.actions = [self.ui.actionSelection,
                        self.ui.actionCreation,
                        self.ui.actionClique,
                        self.ui.actionCycle,
                        self.ui.actionMove,
                        self.ui.actionPath]

        self.graph = nx.DiGraph()

        self._setupActions()
        self.setMode(SelectionMode)

        self.setMouseTracking(True)

        self.leftBipartite = []

        self.loadPlugins()


    @debug.trace()
    def addGraph(self, graphBuilder):
        graphBuilder.build(self, 0, 0)


    @debug.trace()
    def _setupActions(self):
        """Conecta todas las acciones su implementación
        """

        # Acciones relacionadas a los modos
        self.modes = QActionGroup(self)

        for x in self.actions:
            self.modes.addAction(x)

        self.ui.actionSelection.triggered.connect(lambda: self.setMode(SelectionMode))
        self.ui.actionMove.triggered.connect(lambda: self.setMode(MoveMode))
        self.ui.actionCreation.triggered.connect(lambda: self.setMode(CreationMode))
        self.ui.actionClique.triggered.connect(lambda: self.setMode(CliqueMode))
        self.ui.actionCycle.triggered.connect(lambda: self.setMode(CycleMode))
        self.ui.actionPath.triggered.connect(lambda: self.setMode(PathMode))

        # Comandos de nodos
        self.ui.actionMakeClique.triggered.connect(lambda: self.makeClique(self.selectedItems()))
        self.ui.actionMakeCycle.triggered.connect(lambda: self.makeCycle(self.selectedItems()))
        self.ui.actionMakePath.triggered.connect(lambda: self.makePath(self.selectedItems()))
        self.ui.actionRemoveAll.triggered.connect(lambda: self.removeAll(self.selectedItems()))
        self.ui.actionRemoveEdges.triggered.connect(lambda: self.removeAllEdges(self.selectedItems()))
        self.ui.actionSwapEdges.triggered.connect(lambda: self.swapEdges(self.selectedItems()))
        self.ui.actionCompleteEdges.triggered.connect(lambda: self.completeEdges(self.selectedItems()))
        self.ui.actionLeftBipartite.triggered.connect(lambda: self.selectLeftBipartite(self.selectedItems()))
        self.ui.actionCompleteBipartite.triggered.connect(lambda: self.completeBipartite(self.selectedItems()))

        # Comandos de creación de grafos
        self.ui.actionInsertGrid.triggered.connect(lambda: self.addGraph(GridBuilder()))
        self.ui.actionInsertClique.triggered.connect(lambda: self.addGraph(CliqueBuilder()))
        self.ui.actionInsertCycle.triggered.connect(lambda: self.addGraph(CycleBuilder()))
        self.ui.actionInsertPath.triggered.connect(lambda: self.addGraph(PathBuilder()))
        self.ui.actionInsertBipartite.triggered.connect(lambda: self.addGraph(BipartiteBuilder()))


    @debug.trace()
    def selectedItems(self):
        return self.scene.selectedItems()

    @debug.trace()
    def setMode(self, modeType):
        self.mode = modeType(self.ui.graphicsView)

    @debug.trace()
    def graphDoubleClick(self, event):
        self.mode.mouseDoubleClickEvent(self, event)

    @debug.trace()
    def graphWheel(self, event):
        self.scaleView(math.pow(2, -event.delta() / 240.0))

    @debug.trace()
    def addNode(self, point):
        """Añade un nuevo nodo en coordenadas de la escena
        """
        node = GraphicNode(self.ui.graphicsView)

        node.setX(point.x())
        node.setY(point.y())

        self.nodes.append(node)
        self.scene.addItem(node)

        # self.ui.graphicsView.centerOn(node)

        return node

    @debug.trace()
    def addEdge(self, source, dest):
        """Añade una nueva arista entre dos nodos. Si la
        arista existe, entonces no se añade.
        """

        edge =  self.edgesDict.get((source, dest))

        if edge:
            return edge

        edge = GraphicEdge(source, dest, self.ui.graphicsView)

        self.edges.append(edge)
        self.scene.addItem(edge)

        self.edgesDict[(source, dest)] = edge

        return edge

    @debug.trace()
    def makeClique(self, nodes):
        for x in nodes:
            for y in nodes:
                if x != y:
                    self.addEdge(x, y)

    @debug.trace()
    def makeCycle(self, nodes):
        nodes.append(nodes[0])

        for i in range(len(nodes) - 1):
            self.addEdge(nodes[i], nodes[i+1])

    @debug.trace()
    def makePath(self, nodes):
        for i in range(len(nodes) - 1):
            self.addEdge(nodes[i], nodes[i+1])

    @debug.trace()
    def removeEdge(self, source, dest):
        """Elimina la arista entre 'source' y 'dest'.
        """
        if not (source, dest) in self.edgesDict:
            return None

        edge = self.edgesDict.pop((source, dest))

        edge.source.removeEdge(edge)
        edge.dest.removeEdge(edge)

        self.scene.removeItem(edge)

    @debug.trace()
    def removeAll(self, nodes):
        for x in nodes:
            self.removeNode(x)

    @debug.trace()
    def removeNode(self, node):
        for edge in list(node.outEdges):
            self.removeEdge(node, edge.dest)

        for edge in list(node.inEdges):
            self.removeEdge(edge.source, node)

        self.scene.removeItem(node)

    @debug.trace()
    def removeAllEdges(self, nodes):
        for x in nodes:
            for y in nodes:
                self.removeEdge(x, y)

    @debug.trace()
    def swapEdges(self, nodes):
        add = []
        remove = []

        for x in nodes:
            for y in nodes:
                if x != y:
                    if (x,y) in self.edgesDict and not (y,x) in self.edgesDict:
                        remove.append((x,y))
                        add.append((y,x))
                    elif (y,x) in self.edgesDict and not (x,y) in self.edgesDict:
                        remove.append((y,x))
                        add.append((x,y))

        for x,y in add:
            self.addEdge(x,y)

        for x,y in remove:
            self.removeEdge(x,y)

    @debug.trace()
    def completeEdges(self, nodes):
        for x in nodes:
            for y in nodes:
                if (x,y) in self.edgesDict:
                    self.addEdge(y, x)
                elif (y, x) in self.edgesDict:
                    self.addEdge(x, y)

    @debug.trace()
    def group(self, nodes):
        pass

    @debug.trace()
    def unGroup(self, node):
        pass

    @debug.trace()
    def selectLeftBipartite(self, nodes):
        self.leftBipartite = nodes
        self.ui.actionCompleteBipartite.setEnabled(True)

        for x in nodes:
            x.isBipartite = True
            x.update()

    @debug.trace()
    def completeBipartite(self, nodes):
        self.ui.actionCompleteBipartite.setEnabled(False)

        for x in self.leftBipartite:
            for y in nodes:
                self.addEdge(x, y)

        for x in self.leftBipartite:
            x.isBipartite = False
            x.update()

        self.leftBipartite = []

    @debug.trace()
    def scaleView(self, scaleFactor):
        factor = self.ui.graphicsView.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

        if factor < 0.07 or factor > 100:
            return False, factor

        self.ui.graphicsView.scale(scaleFactor, scaleFactor)
        return True, factor

    @debug.trace()
    def loadPlugins(self):
        self._loadCustomBuilders()

    @debug.trace()
    def _loadCustomBuilders(self):
        layout = QVBoxLayout()
        menu = self.ui.menuInsert.addMenu("Custom Graph")

        for item in sorted(pluginManager.getItems("GraphBuilder"), key=lambda x: x.name):
            try:
                icon = QIcon(item.icon)
                action = menu.addAction(icon, item.name)
                action.setToolTip(item.description)
                btn = QCommandLinkButton(item.name, item.description)

                action.triggered.connect(self._customBuilderActionConnection(item))
                btn.clicked.connect(action.triggered)
                btn.setIcon(icon)
                btn.setIconSize(QSize(42,42))

                layout.addWidget(btn)

            except Exception as e:
                debug.warning("Couldn't load custom graph builder {0}. Error: {1}.", (item, e), "plugins")

        layout.addStretch()
        self.ui.pageCustomGraphs.setLayout(layout)

    def _customBuilderActionConnection(self, item):
        return lambda: self.addGraph(item)
