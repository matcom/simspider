# -*- coding: utf8 -*-
from Code import CodeDialog

from FunctionViewer import *
from PropertyViewer import *

import math
from GraphicEdge import GraphicEdge
from GraphicNode import GraphicNode, Subgraph
from NodeType import NodeType
from Rules import RuleDialog
from Simulation.node import Node
from Simulation.simulator import Simulator
from VisualTracker import VisualTracker

import Simulation.gathering as gt
import Simulation.events as ev

from modes import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import QGLWidget

import ui
import debug
import networkx as nx

from Plugins import pluginManager
from config import config

class GraphViewer(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = ui.Ui_GraphViewer()
        self.ui.setupUi(self)

        self.nodes = set()     # Almacena los nodos
        self.edges = set()   # Almacena las aristas
        self.edgesDict = {} # Permite acceder rápidamente a las aristas por (source, dest)
        self.subgraphs = []   # Almacena los subgrafos
        self.mainGraph = Subgraph("Alone", self)

        self.graph = nx.DiGraph()
        self.leftBipartite = []

        self.scene = QGraphicsScene()
        # self.scene.setItemIndexMethod(QGraphicsScene.NoIndex)

        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setAttribute(Qt.WA_Hover)
        self.ui.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.ui.graphicsView.scale(0.5,0.5)

        # Redirigir los eventos del GraphicsView
        self.ui.graphicsView.mouseDoubleClickEvent = self.connectEvent(self.graphDoubleClick, self.ui.graphicsView.mouseDoubleClickEvent)
        self.ui.graphicsView.mousePressEvent = self.connectEvent(self.graphPress, self.ui.graphicsView.mousePressEvent)
        self.ui.graphicsView.mouseReleaseEvent = self.connectEvent(self.graphRelease, self.ui.graphicsView.mouseReleaseEvent)
        self.ui.graphicsView.mouseMoveEvent = self.connectEvent(self.graphMove, self.ui.graphicsView.mouseMoveEvent)
        self.ui.graphicsView.wheelEvent = self.connectEvent(self.graphWheel, self.ui.graphicsView.wheelEvent)

        self.actions = [self.ui.actionSelection,
                        self.ui.actionCreation,
                        self.ui.actionClique,
                        self.ui.actionCycle,
                        self.ui.actionConnect,
                        self.ui.actionPath]

        self._setupActions()
        self.setMode(SelectionMode)
        # self.setMouseTracking(True)

        # Inicializar los menus
        self.viewports = QActionGroup(self)
        self.viewports.addAction(self.ui.actionGlViewport)
        self.viewports.addAction(self.ui.actionStandardViewport)

        self._setupViewportOptions()
        self.loadPlugins()

        self.ui.actionStandard.nodeType = NodeType(self.graph)
        self.ui.actionStandard.nodeType.action = self.ui.actionStandard
        self.ui.actionStandard.triggered.connect(lambda: self.ui.actionStandard.nodeType.edit())

        self.ui.actionAddType.triggered.connect(self.addNodeType)
        self.ui.actionStandardNode.nodeType = self.ui.actionStandard.nodeType

        self.defaultNodeType = self.ui.actionStandardNode.nodeType
        self.ui.actionStandardNode.triggered.connect(lambda: self.setDefaultNodeType(self.ui.actionStandardNode))
        self.nodeTypes = QActionGroup(self)
        self.nodeTypes.addAction(self.ui.actionStandardNode)
        self.ui.actionSetStandard.type = self.defaultNodeType
        self.ui.actionSetStandard.triggered.connect(self._setNodesType(self.ui.actionSetStandard))

        self.ui.graphTree.itemClicked.connect(self.treeItemClicked)

        self.ui.action_Rules_Editor.triggered.connect(lambda: RuleDialog().exec_())
        self.ui.actionCodeEditor.triggered.connect(self.runCode)

        self.setupFunctionViewer()

        self.logger = VisualLogger(self.ui.out)
        debug.addListener(self.logger)
        self.logger.resetFilters()
        self.logger.filter("log", True)

        self.tracker = VisualTracker(self)
        gt.RegisterTracker(self.tracker)
        gt.RegisterTracker(gt.NodeLog())

        self.simulator = Simulator()

        self.simulator.SetInitialEvents([
            ev.SignalAllNodes(self.graph, "Simulation Started", 0),
        ])

        self.ui.actionNext.triggered.connect(self.nextEvent)
        self.ui.actionJump.triggered.connect(self.jumpEvents)

        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.advanceSimulation)

        self.ui.actionPlay.triggered.connect(self.playSimulation)

    # TODO: No está repintando correctamente

    def advanceSimulation(self):
        self.simulator.Simulate(time = self.timer.interval())
        self.ui.graphicsView.scale(0.5, 0.5)
        self.ui.graphicsView.scale(2.0, 2.0)


    def playSimulation(self, bool):
        if bool:
            self.timer.start()
        else:
            self.timer.stop()


    def jumpEvents(self, bool):
        self.simulator.Simulate(events=config.Simulation.get("JumpStep", 100))
        self.ui.graphicsView.scale(0.5, 0.5)
        self.ui.graphicsView.scale(2.0, 2.0)


    def nextEvent(self, bool):
        self.simulator.Simulate(events=1)
        self.ui.graphicsView.scale(0.5, 0.5)
        self.ui.graphicsView.scale(2.0, 2.0)

    def _setNodesType(self, action):
        def run():
            for n in self.selectedNodes():
                n.nodeType.remove(n)
                n.nodeType = action.type
                action.type.add(n)

            action.type.apply()

        return run

    def setupFunctionViewer(self):
        functions = {
            "Triangle" : TriangularFunction(),
            "Square" : SquareFunction(),
            'Trapezoid':TrapezoidFunction(),
            'Singleton': SingletonFunction(),
            'SShapeFunction' : SShapeFunction(),
            'ZShapeFunction' : ZShapeFunction(),
            'PiShapeFunction':PiShapeFunction(),
        }

        variable = Variable("Temperature")

        self.ui.action_Function_Viewer.triggered.connect(lambda: FunctionViewer(functions, variable).exec_())


    def runCode(self):
        import PyQt4.QtCore as QtCore
        import PyQt4.QtGui as QtGui

        dlg = CodeDialog("main", ("graph", ),
                {
                    "debug" : debug,
                    "QtCore" : QtCore,
                    "QtGui" : QtGui,
            },
            self)

        if dlg.exec_():
            method = dlg.compile()
            method(self)


    def treeItemClicked(self, item, column):
        if column == 0 and hasattr(item, "node"):
            item.node.setSelected(True)
        elif column == 1 and hasattr(item, "node"):
            item.node.setNodeVisible(item.checkState(1) == Qt.Checked)


    def setDefaultNodeType(self, action):
        self.defaultNodeType = action.nodeType


    def addNodeType(self):
        text, ok = QInputDialog.getText(self, "Add new node type", "Enter the new type name")

        if not ok or not text:
            return

        action = self.ui.menu_Node_Types.addAction(text)
        action.nodeType = NodeType(self.graph)
        action.nodeType.action = action
        action.nodeType.name = action.text()
        action.triggered.connect(lambda: action.nodeType.edit())

        action2 = self.ui.menuDefault_Node_Type.addAction(text)
        action2.nodeType = action.nodeType
        action2.setCheckable(True)
        self.nodeTypes.addAction(action2)
        action2.triggered.connect(lambda: self.setDefaultNodeType(action2))

        action3 = self.ui.menu_Set_Nodes_Type.addAction(text)
        action3.type = action.nodeType
        action3.triggered.connect(self._setNodesType(action3))

        action.nodeType.edit()


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
        self.ui.actionConnect.triggered.connect(lambda: self.setMode(ConnectMode))
        self.ui.actionCreation.triggered.connect(lambda: self.setMode(CreationMode))
        self.ui.actionClique.triggered.connect(lambda: self.setMode(CliqueMode))
        self.ui.actionCycle.triggered.connect(lambda: self.setMode(CycleMode))
        self.ui.actionPath.triggered.connect(lambda: self.setMode(PathMode))

        # Comandos de nodos
        self.ui.actionMakeClique.triggered.connect(lambda: self.makeClique(self.selectedNodes()))
        self.ui.actionMakeCycle.triggered.connect(lambda: self.makeCycle(self.selectedNodes()))
        self.ui.actionMakePath.triggered.connect(lambda: self.makePath(self.selectedNodes()))
        self.ui.actionRemoveAll.triggered.connect(lambda: self.removeAll(self.selectedNodes(), self.selectedEdges()))
        self.ui.actionRemoveEdges.triggered.connect(lambda: self.removeAllEdges(self.selectedItems(), self.selectedEdges()))
        self.ui.actionSwapEdges.triggered.connect(lambda: self.swapEdges(self.selectedItems(), self.selectedEdges()))
        self.ui.actionCompleteEdges.triggered.connect(lambda: self.completeEdges(self.selectedItems(), self.selectedEdges()))
        self.ui.actionLeftBipartite.triggered.connect(lambda: self.selectLeftBipartite(self.selectedNodes()))
        self.ui.actionCompleteBipartite.triggered.connect(lambda: self.completeBipartite(self.selectedNodes()))

        #Acciones relacionadas con la corrida de la simulación
        self.simul = QActionGroup(self)
        self.simul.addAction(self.ui.actionPlay)
        self.simul.addAction(self.ui.actionPause)
        self.simul.addAction(self.ui.actionNext)
        self.simul.addAction(self.ui.actionJump)

        # Acciones del graph tree
        self.ui.graphTree.itemClicked.connect(lambda item, col: self.selectNode(item))

    def selectNode(self, node):
        self.deselectAll()
        node.setSelected(True)

    @debug.trace()
    def selectedItems(self):
        return self.scene.selectedItems()

    @debug.trace()
    def selectedNodes(self):
        return [x for x in self.selectedItems() if isinstance(x, GraphicNode)]

    @debug.trace()
    def selectedEdges(self):
        return [x for x in self.selectedItems() if isinstance(x, GraphicEdge)]

    @debug.trace()
    def setMode(self, modeType):
        self.mode = modeType(self.ui.graphicsView)

    def graphDoubleClick(self, event):
        return self.mode.mouseDoubleClickEvent(self, event)

    def connectEvent(self, redirect, original):
        def callEvent(event):
            if not redirect(event):
                original(event)
        return callEvent

    def graphPress(self, event):
        return self.mode.mousePressEvent(self, event)

    def graphRelease(self, event):
        return self.mode.mouseReleaseEvent(self, event)

    def graphMove(self, event):
        return self.mode.mouseMoveEvent(self, event)

    def graphWheel(self, event):
        return self.mode.mouseWheel(self, event)

    @debug.trace()
    def addNode(self, point, parent=None):
        """Añade un nuevo nodo en coordenadas de la escena
        """

        if not parent:
            parent = self.mainGraph

        # if len(self.nodes) == self.maxNodes:
        #   QMessageBox.critical(self,
        #         "Max nodes capacity reached",
        #         "The maximun number of nodes that can be displayed has been reached."
        #         "Please consider using the console application instead.")

        #     return None

        node = GraphicNode(self.ui.graphicsView)
        self.graph.add_node(node)
        node.nodeType = self.defaultNodeType
        node.nodeType.add(node)
        node.attributes = Node(self.graph, node)

        # Actualizar el subgrafo
        node.connect(parent)

        node.setX(point.x())
        node.setY(point.y())

        self.nodes.add(node)
        self.scene.addItem(node)

        self.deselectAll()
        node.setSelected(True)

        return node

    def visibleNodes(self):
        return GraphicNode.visibleNodes

    @debug.trace()
    def addEdge(self, source, dest):
        """Añade una nueva arista entre dos nodos. Si la
        arista existe, entonces no se añade.
        """

        edge =  self.edgesDict.get((source, dest))

        if edge:
            return edge

        edge = GraphicEdge(source, dest, self.ui.graphicsView)

        self.edges.add(edge)
        self.scene.addItem(edge)

        self.edgesDict[(source, dest)] = edge
        self.graph.add_edge(source, dest)

        if not edge.dest.isVisible() or not edge.source.isVisible():
            edge.setVisible(False)

        return edge

    @debug.trace()
    def makeClique(self, nodes):
        if not nodes:
            return

        for x in nodes:
            for y in nodes:
                if x != y:
                    self.addEdge(x, y)

    @debug.trace()
    def makeCycle(self, nodes):
        if not nodes:
            return

        nodes.append(nodes[0])

        for i in range(len(nodes) - 1):
            self.addEdge(nodes[i], nodes[i+1])

    @debug.trace()
    def makePath(self, nodes):
        if not nodes:
            return

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
        self.edges.remove(edge)
        self.graph.remove_edge(source, dest)
        self.scene.removeItem(edge)

    @debug.trace()
    def removeAll(self, nodes, edges):
        for x in nodes:
            self.removeNode(x)

        for y in edges:
            self.removeEdge(y.source, y.dest)

    @debug.trace()
    def removeNode(self, node):
        for edge in list(node.outEdges):
            self.removeEdge(node, edge.dest)

        for edge in list(node.inEdges):
            self.removeEdge(edge.source, node)

        subgraph = node.subgraph
        node.disconnect()

        if not subgraph.nodes and subgraph != self.mainGraph:
            subgraph.delete()

        if node.isVisible():
            GraphicNode.visibleNodes -= 1

        node.nodeType.remove(node)

        self.nodes.remove(node)
        self.graph.remove_node(node)
        self.scene.removeItem(node)

    @debug.trace()
    def removeAllEdges(self, nodes, edges):
        for x in nodes:
            for y in nodes:
                self.removeEdge(x, y)

        for y in edges:
            self.removeEdge(y.source, y.dest)


    @debug.trace()
    def swapEdges(self, nodes, edges):
        add = []
        remove = []

        for e in edges:
            if not e.source in nodes:
                nodes.append(e.source)
            if not e.dest in nodes:
                nodes.append(e.dest)

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
    def completeEdges(self, nodes, edges):
        for e in edges:
            if not e.source in nodes:
                nodes.append(e.source)
            if not e.dest in nodes:
                nodes.append(e.dest)

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
        self._loadLayoutPlugins()
        self._loadGeneralPlugins()


    @debug.trace()
    def _loadCustomBuilders(self):
        items = pluginManager.getItems("GraphBuilder")
        itemsDict = {}

        for item in items:
            list = []

            if item.group in itemsDict:
                list = itemsDict[item.group]
            else:
                itemsDict[item.group] = list

            list.append(item)

        for group, itemList in itemsDict.items():
            self._loadCustomBuildersGroup(group, itemList)

    def _customBuilderActionConnection(self, item):
        return lambda: self.addGraph(item)

    def _setupViewportOptions(self):
        self.ui.actionGlViewport.triggered.connect(lambda: self.ui.graphicsView.setViewport(QGLWidget()))
        self.ui.actionStandardViewport.triggered.connect(lambda: self.ui.graphicsView.setViewport(None))

        self.ui.actionAntialiasing.triggered.connect(
            lambda b: self.ui.graphicsView.setRenderHint(QPainter.Antialiasing, b))
        self.ui.actionText_Antialiasing.triggered.connect(
            lambda b: self.ui.graphicsView.setRenderHint(QPainter.TextAntialiasing, b))
        self.ui.actionHigh_Quality_Antialiasing.triggered.connect(
            lambda b: self.ui.graphicsView.setRenderHint(QPainter.HighQualityAntialiasing, b))
        self.ui.actionSmooth_Pixmap_Transform.triggered.connect(
            lambda b: self.ui.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform, b))

    def _loadCustomBuildersGroup(self, group, itemsList):
        if group == "Basic":
            page = self.ui.pageBasic
            layout = page.layout()
        else:
            page = QWidget()
            self.ui.graphToolBox.addItem(page, group)
            layout = QVBoxLayout()

        menu = self.ui.menuInsert.addMenu("{0} Graphs".format(group))

        for item in sorted(itemsList, key=lambda x: x.name):
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

        if group != "Basic":
            page.setLayout(layout)

    @debug.trace()
    def itemsAt(self, x, y):
        return self.ui.graphicsView.items(x,y)

    @debug.trace()
    def edgesAt(self, x, y):
        return [e for e in self.itemsAt(x,y) if isinstance(e, GraphicEdge)]

    @debug.trace()
    def nodesAt(self, x, y):
        return [n for n in self.itemsAt(x,y) if isinstance(n, GraphicNode)]

    @debug.trace()
    def insertNode(self, node, edge):
        self.addEdge(edge.source, node)
        self.addEdge(node, edge.dest)
        self.removeEdge(edge.source, edge.dest)

    def deselectAll(self):
        for item in self.selectedItems():
            item.setSelected(False)

    def _loadGeneralPlugins(self):
        required = ["name", "description", "install", "uninstall"]

        for plugin in pluginManager.getItems("GeneralPlugin"):
            for attr in required:
                if not hasattr(plugin, attr):
                    continue

            self._loadGeneralPlugin(plugin)

    def _loadGeneralPlugin(self, plugin):
        action = self.ui.menuPlugins.addAction(plugin.name)
        action.setCheckable(True)
        action.setTooltip(plugin.description)
        action.setEnabled(False)

    def _loadLayoutPlugins(self):
        for item in pluginManager.getItems("Layout"):
            action = self.ui.menu_Layout.addAction(item.name)
            action.setToolTip(item.description)
            action.setIcon(QIcon(item.icon))
            action.triggered.connect(self._connectLayout(item))

    def _applyLayout(self, item):
        nodes = list(self.selectedNodes())
        item.apply(nodes)

        if self.ui.actionAnimations.isChecked():
            animation = QParallelAnimationGroup(self)

            for n in nodes:
                animX = QPropertyAnimation(n, "x")
                animX.setEndValue(n.newX)

                animY = QPropertyAnimation(n, "y")
                animY.setEndValue(n.newY)

                debug.debug("Animating node from ({0},{1}) to ({2},{3})", (n.x(), n.y(), n.newX, n.newY),
                    "graphviewer.animations")

                animation.addAnimation(animX)
                animation.addAnimation(animY)

            debug.info("Starting layout animation", (), "graphviewer.animations")
            animation.start()

        else:
            for n in nodes:
                n.setX(n.newX)
                n.setY(n.newY)


    def _connectLayout(self, item):
        def apply():
            self._applyLayout(item)
        return apply


class VisualLogger(debug.TraceListener):
    def __init__(self, out):
        super().__init__()
        self.out = out

    def output(self, msg, args = ()):
        self.out.setPlainText(self.out.toPlainText() + "\n" + msg.format(*args))
