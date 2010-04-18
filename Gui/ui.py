# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GraphViewer.ui'
#
# Created: Tue May 22 22:09:11 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GraphViewer(object):
    def setupUi(self, GraphViewer):
        GraphViewer.setObjectName(_fromUtf8("GraphViewer"))
        GraphViewer.resize(872, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Clique.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GraphViewer.setWindowIcon(icon)
        GraphViewer.setIconSize(QtCore.QSize(32, 32))
        GraphViewer.setAnimated(False)
        self.centralwidget = QtGui.QWidget(GraphViewer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        GraphViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GraphViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTransform = QtGui.QMenu(self.menubar)
        self.menuTransform.setObjectName(_fromUtf8("menuTransform"))
        self.menuInsert = QtGui.QMenu(self.menubar)
        self.menuInsert.setObjectName(_fromUtf8("menuInsert"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menu_Viewport = QtGui.QMenu(self.menu_View)
        self.menu_Viewport.setObjectName(_fromUtf8("menu_Viewport"))
        self.menuRender_Hints = QtGui.QMenu(self.menu_Viewport)
        self.menuRender_Hints.setObjectName(_fromUtf8("menuRender_Hints"))
        self.menuPlugins = QtGui.QMenu(self.menubar)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        self.menu_Layout = QtGui.QMenu(self.menubar)
        self.menu_Layout.setObjectName(_fromUtf8("menu_Layout"))
        GraphViewer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GraphViewer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GraphViewer.setStatusBar(self.statusbar)
        self.toolBoxDock = QtGui.QDockWidget(GraphViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBoxDock.sizePolicy().hasHeightForWidth())
        self.toolBoxDock.setSizePolicy(sizePolicy)
        self.toolBoxDock.setMinimumSize(QtCore.QSize(320, 190))
        self.toolBoxDock.setObjectName(_fromUtf8("toolBoxDock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.pageModes = QtGui.QWidget()
        self.pageModes.setGeometry(QtCore.QRect(0, 0, 285, 466))
        self.pageModes.setObjectName(_fromUtf8("pageModes"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.pageModes)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnSelection = QtGui.QCommandLinkButton(self.pageModes)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelection.setIcon(icon1)
        self.btnSelection.setIconSize(QtCore.QSize(42, 42))
        self.btnSelection.setCheckable(True)
        self.btnSelection.setChecked(True)
        self.btnSelection.setObjectName(_fromUtf8("btnSelection"))
        self.buttonGroup = QtGui.QButtonGroup(GraphViewer)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.btnSelection)
        self.verticalLayout_2.addWidget(self.btnSelection)
        self.btnAddNode = QtGui.QCommandLinkButton(self.pageModes)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Create.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddNode.setIcon(icon2)
        self.btnAddNode.setIconSize(QtCore.QSize(42, 42))
        self.btnAddNode.setCheckable(True)
        self.btnAddNode.setObjectName(_fromUtf8("btnAddNode"))
        self.buttonGroup.addButton(self.btnAddNode)
        self.verticalLayout_2.addWidget(self.btnAddNode)
        self.btnClique = QtGui.QCommandLinkButton(self.pageModes)
        self.btnClique.setIcon(icon)
        self.btnClique.setIconSize(QtCore.QSize(42, 42))
        self.btnClique.setCheckable(True)
        self.btnClique.setObjectName(_fromUtf8("btnClique"))
        self.buttonGroup.addButton(self.btnClique)
        self.verticalLayout_2.addWidget(self.btnClique)
        self.btnCycle = QtGui.QCommandLinkButton(self.pageModes)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Cycle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCycle.setIcon(icon3)
        self.btnCycle.setIconSize(QtCore.QSize(42, 42))
        self.btnCycle.setCheckable(True)
        self.btnCycle.setObjectName(_fromUtf8("btnCycle"))
        self.buttonGroup.addButton(self.btnCycle)
        self.verticalLayout_2.addWidget(self.btnCycle)
        self.btnPath = QtGui.QCommandLinkButton(self.pageModes)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Path.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPath.setIcon(icon4)
        self.btnPath.setIconSize(QtCore.QSize(42, 42))
        self.btnPath.setCheckable(True)
        self.btnPath.setObjectName(_fromUtf8("btnPath"))
        self.buttonGroup.addButton(self.btnPath)
        self.verticalLayout_2.addWidget(self.btnPath)
        self.btnMove = QtGui.QCommandLinkButton(self.pageModes)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Move.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMove.setIcon(icon5)
        self.btnMove.setIconSize(QtCore.QSize(42, 42))
        self.btnMove.setCheckable(True)
        self.btnMove.setObjectName(_fromUtf8("btnMove"))
        self.buttonGroup.addButton(self.btnMove)
        self.verticalLayout_2.addWidget(self.btnMove)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolBox.addItem(self.pageModes, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBox)
        self.toolBoxDock.setWidget(self.dockWidgetContents)
        GraphViewer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolBoxDock)
        self.modesToolbar = QtGui.QToolBar(GraphViewer)
        self.modesToolbar.setIconSize(QtCore.QSize(42, 42))
        self.modesToolbar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.modesToolbar.setObjectName(_fromUtf8("modesToolbar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.modesToolbar)
        self.graphDock = QtGui.QDockWidget(GraphViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphDock.sizePolicy().hasHeightForWidth())
        self.graphDock.setSizePolicy(sizePolicy)
        self.graphDock.setMinimumSize(QtCore.QSize(320, 136))
        self.graphDock.setObjectName(_fromUtf8("graphDock"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphToolBox = QtGui.QToolBox(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphToolBox.sizePolicy().hasHeightForWidth())
        self.graphToolBox.setSizePolicy(sizePolicy)
        self.graphToolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.graphToolBox.setObjectName(_fromUtf8("graphToolBox"))
        self.pageBasic = QtGui.QWidget()
        self.pageBasic.setGeometry(QtCore.QRect(0, 0, 302, 69))
        self.pageBasic.setObjectName(_fromUtf8("pageBasic"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pageBasic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphToolBox.addItem(self.pageBasic, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.graphToolBox, 0, 0, 1, 1)
        self.graphDock.setWidget(self.dockWidgetContents_2)
        GraphViewer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.graphDock)
        self.graphViewer = QtGui.QDockWidget(GraphViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphViewer.sizePolicy().hasHeightForWidth())
        self.graphViewer.setSizePolicy(sizePolicy)
        self.graphViewer.setFloating(False)
        self.graphViewer.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.graphViewer.setObjectName(_fromUtf8("graphViewer"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.dockWidgetContents_3)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.graphicsView.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.graphicsView.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.graphViewer.setWidget(self.dockWidgetContents_3)
        GraphViewer.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.graphViewer)
        self.designToolbar = QtGui.QToolBar(GraphViewer)
        self.designToolbar.setIconSize(QtCore.QSize(42, 42))
        self.designToolbar.setObjectName(_fromUtf8("designToolbar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.designToolbar)
        self.deleteToolbar = QtGui.QToolBar(GraphViewer)
        self.deleteToolbar.setIconSize(QtCore.QSize(42, 42))
        self.deleteToolbar.setObjectName(_fromUtf8("deleteToolbar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.deleteToolbar)
        self.bipartiteToolbar = QtGui.QToolBar(GraphViewer)
        self.bipartiteToolbar.setIconSize(QtCore.QSize(42, 42))
        self.bipartiteToolbar.setObjectName(_fromUtf8("bipartiteToolbar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.bipartiteToolbar)
        self.edgesToolbar = QtGui.QToolBar(GraphViewer)
        self.edgesToolbar.setIconSize(QtCore.QSize(42, 42))
        self.edgesToolbar.setObjectName(_fromUtf8("edgesToolbar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.edgesToolbar)
        self.actionSelection = QtGui.QAction(GraphViewer)
        self.actionSelection.setCheckable(True)
        self.actionSelection.setChecked(True)
        self.actionSelection.setIcon(icon1)
        self.actionSelection.setObjectName(_fromUtf8("actionSelection"))
        self.actionCreation = QtGui.QAction(GraphViewer)
        self.actionCreation.setCheckable(True)
        self.actionCreation.setChecked(False)
        self.actionCreation.setIcon(icon2)
        self.actionCreation.setObjectName(_fromUtf8("actionCreation"))
        self.actionQuit = QtGui.QAction(GraphViewer)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionMove = QtGui.QAction(GraphViewer)
        self.actionMove.setCheckable(True)
        self.actionMove.setIcon(icon5)
        self.actionMove.setObjectName(_fromUtf8("actionMove"))
        self.actionClique = QtGui.QAction(GraphViewer)
        self.actionClique.setCheckable(True)
        self.actionClique.setIcon(icon)
        self.actionClique.setObjectName(_fromUtf8("actionClique"))
        self.actionCycle = QtGui.QAction(GraphViewer)
        self.actionCycle.setCheckable(True)
        self.actionCycle.setIcon(icon3)
        self.actionCycle.setObjectName(_fromUtf8("actionCycle"))
        self.actionMakeClique = QtGui.QAction(GraphViewer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakeClique.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakeClique.setIcon(icon6)
        self.actionMakeClique.setObjectName(_fromUtf8("actionMakeClique"))
        self.actionMakeCycle = QtGui.QAction(GraphViewer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakeCycle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakeCycle.setIcon(icon7)
        self.actionMakeCycle.setObjectName(_fromUtf8("actionMakeCycle"))
        self.actionMakePath = QtGui.QAction(GraphViewer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakePath.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakePath.setIcon(icon8)
        self.actionMakePath.setObjectName(_fromUtf8("actionMakePath"))
        self.actionPath = QtGui.QAction(GraphViewer)
        self.actionPath.setCheckable(True)
        self.actionPath.setIcon(icon4)
        self.actionPath.setObjectName(_fromUtf8("actionPath"))
        self.actionRemoveAll = QtGui.QAction(GraphViewer)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RemoveAll.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveAll.setIcon(icon9)
        self.actionRemoveAll.setObjectName(_fromUtf8("actionRemoveAll"))
        self.actionRemoveEdges = QtGui.QAction(GraphViewer)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RemoveEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveEdges.setIcon(icon10)
        self.actionRemoveEdges.setObjectName(_fromUtf8("actionRemoveEdges"))
        self.actionSwapEdges = QtGui.QAction(GraphViewer)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/SwapEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSwapEdges.setIcon(icon11)
        self.actionSwapEdges.setObjectName(_fromUtf8("actionSwapEdges"))
        self.actionCompleteEdges = QtGui.QAction(GraphViewer)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/CompleteEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompleteEdges.setIcon(icon12)
        self.actionCompleteEdges.setObjectName(_fromUtf8("actionCompleteEdges"))
        self.actionLeftBipartite = QtGui.QAction(GraphViewer)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/LeftBipartite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeftBipartite.setIcon(icon13)
        self.actionLeftBipartite.setObjectName(_fromUtf8("actionLeftBipartite"))
        self.actionCompleteBipartite = QtGui.QAction(GraphViewer)
        self.actionCompleteBipartite.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RightBipartite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompleteBipartite.setIcon(icon14)
        self.actionCompleteBipartite.setObjectName(_fromUtf8("actionCompleteBipartite"))
        self.actionGlViewport = QtGui.QAction(GraphViewer)
        self.actionGlViewport.setCheckable(True)
        self.actionGlViewport.setObjectName(_fromUtf8("actionGlViewport"))
        self.actionStandardViewport = QtGui.QAction(GraphViewer)
        self.actionStandardViewport.setCheckable(True)
        self.actionStandardViewport.setChecked(True)
        self.actionStandardViewport.setObjectName(_fromUtf8("actionStandardViewport"))
        self.actionAnimations = QtGui.QAction(GraphViewer)
        self.actionAnimations.setCheckable(True)
        self.actionAnimations.setChecked(True)
        self.actionAnimations.setObjectName(_fromUtf8("actionAnimations"))
        self.actionAntialiasing = QtGui.QAction(GraphViewer)
        self.actionAntialiasing.setCheckable(True)
        self.actionAntialiasing.setChecked(True)
        self.actionAntialiasing.setObjectName(_fromUtf8("actionAntialiasing"))
        self.actionText_Antialiasing = QtGui.QAction(GraphViewer)
        self.actionText_Antialiasing.setCheckable(True)
        self.actionText_Antialiasing.setChecked(True)
        self.actionText_Antialiasing.setObjectName(_fromUtf8("actionText_Antialiasing"))
        self.actionSmooth_Pixmap_Transform = QtGui.QAction(GraphViewer)
        self.actionSmooth_Pixmap_Transform.setCheckable(True)
        self.actionSmooth_Pixmap_Transform.setObjectName(_fromUtf8("actionSmooth_Pixmap_Transform"))
        self.actionHigh_Quality_Antialiasing = QtGui.QAction(GraphViewer)
        self.actionHigh_Quality_Antialiasing.setCheckable(True)
        self.actionHigh_Quality_Antialiasing.setObjectName(_fromUtf8("actionHigh_Quality_Antialiasing"))
        self.menuFile.addAction(self.actionQuit)
        self.menuTransform.addAction(self.actionSelection)
        self.menuTransform.addAction(self.actionClique)
        self.menuTransform.addAction(self.actionCycle)
        self.menuTransform.addAction(self.actionPath)
        self.menuTransform.addAction(self.actionMove)
        self.menuTransform.addSeparator()
        self.menuTransform.addAction(self.actionMakeClique)
        self.menuTransform.addAction(self.actionMakeCycle)
        self.menuTransform.addAction(self.actionMakePath)
        self.menuTransform.addSeparator()
        self.menuTransform.addAction(self.actionLeftBipartite)
        self.menuTransform.addAction(self.actionCompleteBipartite)
        self.menuTransform.addSeparator()
        self.menuTransform.addAction(self.actionRemoveAll)
        self.menuTransform.addAction(self.actionRemoveEdges)
        self.menuTransform.addSeparator()
        self.menuTransform.addAction(self.actionSwapEdges)
        self.menuTransform.addAction(self.actionCompleteEdges)
        self.menuRender_Hints.addAction(self.actionAntialiasing)
        self.menuRender_Hints.addAction(self.actionText_Antialiasing)
        self.menuRender_Hints.addAction(self.actionSmooth_Pixmap_Transform)
        self.menuRender_Hints.addAction(self.actionHigh_Quality_Antialiasing)
        self.menu_Viewport.addAction(self.actionGlViewport)
        self.menu_Viewport.addAction(self.actionStandardViewport)
        self.menu_Viewport.addSeparator()
        self.menu_Viewport.addAction(self.menuRender_Hints.menuAction())
        self.menu_View.addAction(self.actionAnimations)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.menu_Viewport.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menu_Layout.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.modesToolbar.addAction(self.actionSelection)
        self.modesToolbar.addAction(self.actionCreation)
        self.modesToolbar.addAction(self.actionClique)
        self.modesToolbar.addAction(self.actionCycle)
        self.modesToolbar.addAction(self.actionPath)
        self.modesToolbar.addAction(self.actionMove)
        self.designToolbar.addAction(self.actionMakeClique)
        self.designToolbar.addAction(self.actionMakeCycle)
        self.designToolbar.addAction(self.actionMakePath)
        self.deleteToolbar.addAction(self.actionRemoveAll)
        self.deleteToolbar.addAction(self.actionRemoveEdges)
        self.bipartiteToolbar.addAction(self.actionLeftBipartite)
        self.bipartiteToolbar.addAction(self.actionCompleteBipartite)
        self.edgesToolbar.addAction(self.actionSwapEdges)
        self.edgesToolbar.addAction(self.actionCompleteEdges)

        self.retranslateUi(GraphViewer)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        self.graphToolBox.setCurrentIndex(0)
        self.graphToolBox.layout().setSpacing(6)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), GraphViewer.close)
        QtCore.QObject.connect(self.btnSelection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.actionSelection.setChecked)
        QtCore.QObject.connect(self.btnAddNode, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionCreation.setChecked)
        QtCore.QObject.connect(self.btnClique, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionClique.setChecked)
        QtCore.QObject.connect(self.btnCycle, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionCycle.setChecked)
        QtCore.QObject.connect(self.btnPath, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionPath.setChecked)
        QtCore.QObject.connect(self.btnMove, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.actionMove.setChecked)
        QtCore.QObject.connect(self.actionSelection, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnSelection.setChecked)
        QtCore.QObject.connect(self.actionCreation, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnAddNode.setChecked)
        QtCore.QObject.connect(self.actionClique, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnClique.setChecked)
        QtCore.QObject.connect(self.actionCycle, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnCycle.setChecked)
        QtCore.QObject.connect(self.actionPath, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnPath.setChecked)
        QtCore.QObject.connect(self.actionMove, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.btnMove.setChecked)
        QtCore.QMetaObject.connectSlotsByName(GraphViewer)

    def retranslateUi(self, GraphViewer):
        GraphViewer.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("GraphViewer", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTransform.setTitle(QtGui.QApplication.translate("GraphViewer", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert.setTitle(QtGui.QApplication.translate("GraphViewer", "&Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("GraphViewer", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Viewport.setTitle(QtGui.QApplication.translate("GraphViewer", "&Viewport", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRender_Hints.setTitle(QtGui.QApplication.translate("GraphViewer", "Render Hints", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("GraphViewer", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Layout.setTitle(QtGui.QApplication.translate("GraphViewer", "&Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxDock.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelection.setText(QtGui.QApplication.translate("GraphViewer", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelection.setDescription(QtGui.QApplication.translate("GraphViewer", "Select multiple nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddNode.setText(QtGui.QApplication.translate("GraphViewer", "Add Node", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddNode.setDescription(QtGui.QApplication.translate("GraphViewer", "Add independent nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClique.setText(QtGui.QApplication.translate("GraphViewer", "Create Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClique.setDescription(QtGui.QApplication.translate("GraphViewer", "Add nodes to create a clique", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCycle.setText(QtGui.QApplication.translate("GraphViewer", "Create Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCycle.setDescription(QtGui.QApplication.translate("GraphViewer", "Add nodes to create a cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPath.setText(QtGui.QApplication.translate("GraphViewer", "Create Path", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPath.setDescription(QtGui.QApplication.translate("GraphViewer", "Add nodes to create a path", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setText(QtGui.QApplication.translate("GraphViewer", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setDescription(QtGui.QApplication.translate("GraphViewer", "Click and drag to navigate", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageModes), QtGui.QApplication.translate("GraphViewer", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.modesToolbar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Modes Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.graphDock.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.graphToolBox.setItemText(self.graphToolBox.indexOf(self.pageBasic), QtGui.QApplication.translate("GraphViewer", "Basic", None, QtGui.QApplication.UnicodeUTF8))
        self.graphViewer.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Graph Visualizer", None, QtGui.QApplication.UnicodeUTF8))
        self.designToolbar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Design Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteToolbar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Remove Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.bipartiteToolbar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Bipartite Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.edgesToolbar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Edges Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setText(QtGui.QApplication.translate("GraphViewer", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to select several nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreation.setText(QtGui.QApplication.translate("GraphViewer", "Add Node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreation.setToolTip(QtGui.QApplication.translate("GraphViewer", "Adds a new node with double click", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreation.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("GraphViewer", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("GraphViewer", "Exit the graph creation tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("GraphViewer", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setText(QtGui.QApplication.translate("GraphViewer", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to drag the scene to move", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClique.setText(QtGui.QApplication.translate("GraphViewer", "Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClique.setToolTip(QtGui.QApplication.translate("GraphViewer", "New nodes will make a clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClique.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCycle.setText(QtGui.QApplication.translate("GraphViewer", "Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCycle.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeClique.setText(QtGui.QApplication.translate("GraphViewer", "Make Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeClique.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a clique from all selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeClique.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeCycle.setText(QtGui.QApplication.translate("GraphViewer", "Make Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeCycle.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a cycle between all selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeCycle.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakePath.setText(QtGui.QApplication.translate("GraphViewer", "Make Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakePath.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a path between all selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakePath.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPath.setText(QtGui.QApplication.translate("GraphViewer", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPath.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to build a path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPath.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setText(QtGui.QApplication.translate("GraphViewer", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setToolTip(QtGui.QApplication.translate("GraphViewer", "Deletes all nodes selected and all related edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setShortcut(QtGui.QApplication.translate("GraphViewer", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveEdges.setText(QtGui.QApplication.translate("GraphViewer", "Remove Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Deletes all edges between any pair of selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveEdges.setShortcut(QtGui.QApplication.translate("GraphViewer", "Shift+Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwapEdges.setText(QtGui.QApplication.translate("GraphViewer", "Swap Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwapEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Swaps all the edges between selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwapEdges.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteEdges.setText(QtGui.QApplication.translate("GraphViewer", "Complete Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Adds the symetric edge for all edges between the nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteEdges.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeftBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Select Left Bipartite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeftBipartite.setToolTip(QtGui.QApplication.translate("GraphViewer", "Mark the selected nodes to be used later for a bipartite graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeftBipartite.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Complete Bipartite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteBipartite.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a bipartite graph with the currently selected and the previously selected ones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteBipartite.setShortcut(QtGui.QApplication.translate("GraphViewer", "Alt+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGlViewport.setText(QtGui.QApplication.translate("GraphViewer", "OpenGl", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGlViewport.setToolTip(QtGui.QApplication.translate("GraphViewer", "Toggle the viewport to use OpenGl", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStandardViewport.setText(QtGui.QApplication.translate("GraphViewer", "Standard", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStandardViewport.setToolTip(QtGui.QApplication.translate("GraphViewer", "Toggle viewport to use a standard rendering engine", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnimations.setText(QtGui.QApplication.translate("GraphViewer", "Animations", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAntialiasing.setText(QtGui.QApplication.translate("GraphViewer", "Antialiasing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionText_Antialiasing.setText(QtGui.QApplication.translate("GraphViewer", "Text Antialiasing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSmooth_Pixmap_Transform.setText(QtGui.QApplication.translate("GraphViewer", "Smooth Pixmap Transform", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHigh_Quality_Antialiasing.setText(QtGui.QApplication.translate("GraphViewer", "High Quality Antialiasing", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PropertyViewer.ui'
#
# Created: Tue May 22 22:09:11 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PropertyViewer(object):
    def setupUi(self, PropertyViewer):
        PropertyViewer.setObjectName(_fromUtf8("PropertyViewer"))
        PropertyViewer.resize(262, 258)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PropertyViewer.sizePolicy().hasHeightForWidth())
        PropertyViewer.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(PropertyViewer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(PropertyViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 242, 207))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnCancel = QtGui.QPushButton(PropertyViewer)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnOk = QtGui.QPushButton(PropertyViewer)
        self.btnOk.setIconSize(QtCore.QSize(32, 32))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout.addWidget(self.btnOk)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PropertyViewer)
        QtCore.QObject.connect(self.btnOk, QtCore.SIGNAL(_fromUtf8("clicked()")), PropertyViewer.accept)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), PropertyViewer.reject)
        QtCore.QMetaObject.connectSlotsByName(PropertyViewer)

    def retranslateUi(self, PropertyViewer):
        PropertyViewer.setWindowTitle(QtGui.QApplication.translate("PropertyViewer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("PropertyViewer", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("PropertyViewer", "Ok", None, QtGui.QApplication.UnicodeUTF8))

