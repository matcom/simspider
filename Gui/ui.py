# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GraphViewer.ui'
#
# Created: Sun May 20 00:36:24 2012
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
        self.centralwidget = QtGui.QWidget(GraphViewer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.graphicsView.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.graphicsView.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
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
        GraphViewer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GraphViewer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GraphViewer.setStatusBar(self.statusbar)
        self.toolbox = QtGui.QDockWidget(GraphViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbox.sizePolicy().hasHeightForWidth())
        self.toolbox.setSizePolicy(sizePolicy)
        self.toolbox.setMinimumSize(QtCore.QSize(320, 190))
        self.toolbox.setObjectName(_fromUtf8("toolbox"))
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
        self.pageModes.setGeometry(QtCore.QRect(0, -81, 285, 466))
        self.pageModes.setObjectName(_fromUtf8("pageModes"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.pageModes)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnSelection = QtGui.QCommandLinkButton(self.pageModes)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelection.setIcon(icon)
        self.btnSelection.setIconSize(QtCore.QSize(42, 42))
        self.btnSelection.setCheckable(True)
        self.btnSelection.setChecked(True)
        self.btnSelection.setObjectName(_fromUtf8("btnSelection"))
        self.buttonGroup = QtGui.QButtonGroup(GraphViewer)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.btnSelection)
        self.verticalLayout_2.addWidget(self.btnSelection)
        self.btnAddNode = QtGui.QCommandLinkButton(self.pageModes)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Create.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddNode.setIcon(icon1)
        self.btnAddNode.setIconSize(QtCore.QSize(42, 42))
        self.btnAddNode.setCheckable(True)
        self.btnAddNode.setObjectName(_fromUtf8("btnAddNode"))
        self.buttonGroup.addButton(self.btnAddNode)
        self.verticalLayout_2.addWidget(self.btnAddNode)
        self.btnClique = QtGui.QCommandLinkButton(self.pageModes)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Clique.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClique.setIcon(icon2)
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
        self.pageBasic = QtGui.QWidget()
        self.pageBasic.setGeometry(QtCore.QRect(0, 0, 302, 358))
        self.pageBasic.setObjectName(_fromUtf8("pageBasic"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pageBasic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnInsertGrid = QtGui.QCommandLinkButton(self.pageBasic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertGrid.sizePolicy().hasHeightForWidth())
        self.btnInsertGrid.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Grid.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInsertGrid.setIcon(icon6)
        self.btnInsertGrid.setIconSize(QtCore.QSize(42, 42))
        self.btnInsertGrid.setCheckable(False)
        self.btnInsertGrid.setChecked(False)
        self.btnInsertGrid.setObjectName(_fromUtf8("btnInsertGrid"))
        self.verticalLayout.addWidget(self.btnInsertGrid)
        self.btnInsertClique = QtGui.QCommandLinkButton(self.pageBasic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertClique.sizePolicy().hasHeightForWidth())
        self.btnInsertClique.setSizePolicy(sizePolicy)
        self.btnInsertClique.setIcon(icon2)
        self.btnInsertClique.setIconSize(QtCore.QSize(42, 42))
        self.btnInsertClique.setCheckable(False)
        self.btnInsertClique.setChecked(False)
        self.btnInsertClique.setObjectName(_fromUtf8("btnInsertClique"))
        self.verticalLayout.addWidget(self.btnInsertClique)
        self.btnInsertCycle = QtGui.QCommandLinkButton(self.pageBasic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertCycle.sizePolicy().hasHeightForWidth())
        self.btnInsertCycle.setSizePolicy(sizePolicy)
        self.btnInsertCycle.setIcon(icon3)
        self.btnInsertCycle.setIconSize(QtCore.QSize(42, 42))
        self.btnInsertCycle.setCheckable(False)
        self.btnInsertCycle.setChecked(False)
        self.btnInsertCycle.setObjectName(_fromUtf8("btnInsertCycle"))
        self.verticalLayout.addWidget(self.btnInsertCycle)
        self.btnInsertPath = QtGui.QCommandLinkButton(self.pageBasic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertPath.sizePolicy().hasHeightForWidth())
        self.btnInsertPath.setSizePolicy(sizePolicy)
        self.btnInsertPath.setIcon(icon4)
        self.btnInsertPath.setIconSize(QtCore.QSize(42, 42))
        self.btnInsertPath.setCheckable(False)
        self.btnInsertPath.setChecked(False)
        self.btnInsertPath.setObjectName(_fromUtf8("btnInsertPath"))
        self.verticalLayout.addWidget(self.btnInsertPath)
        self.btnInsertBipartite = QtGui.QCommandLinkButton(self.pageBasic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertBipartite.sizePolicy().hasHeightForWidth())
        self.btnInsertBipartite.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Bipartite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInsertBipartite.setIcon(icon7)
        self.btnInsertBipartite.setIconSize(QtCore.QSize(42, 42))
        self.btnInsertBipartite.setCheckable(False)
        self.btnInsertBipartite.setChecked(False)
        self.btnInsertBipartite.setObjectName(_fromUtf8("btnInsertBipartite"))
        self.verticalLayout.addWidget(self.btnInsertBipartite)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.toolBox.addItem(self.pageBasic, _fromUtf8(""))
        self.pageCustomGraphs = QtGui.QWidget()
        self.pageCustomGraphs.setObjectName(_fromUtf8("pageCustomGraphs"))
        self.toolBox.addItem(self.pageCustomGraphs, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBox)
        self.toolbox.setWidget(self.dockWidgetContents)
        GraphViewer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolbox)
        self.toolBar = QtGui.QToolBar(GraphViewer)
        self.toolBar.setIconSize(QtCore.QSize(42, 42))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelection = QtGui.QAction(GraphViewer)
        self.actionSelection.setCheckable(True)
        self.actionSelection.setChecked(True)
        self.actionSelection.setIcon(icon)
        self.actionSelection.setObjectName(_fromUtf8("actionSelection"))
        self.actionCreation = QtGui.QAction(GraphViewer)
        self.actionCreation.setCheckable(True)
        self.actionCreation.setChecked(False)
        self.actionCreation.setIcon(icon1)
        self.actionCreation.setObjectName(_fromUtf8("actionCreation"))
        self.actionQuit = QtGui.QAction(GraphViewer)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionMove = QtGui.QAction(GraphViewer)
        self.actionMove.setCheckable(True)
        self.actionMove.setIcon(icon5)
        self.actionMove.setObjectName(_fromUtf8("actionMove"))
        self.actionClique = QtGui.QAction(GraphViewer)
        self.actionClique.setCheckable(True)
        self.actionClique.setIcon(icon2)
        self.actionClique.setObjectName(_fromUtf8("actionClique"))
        self.actionCycle = QtGui.QAction(GraphViewer)
        self.actionCycle.setCheckable(True)
        self.actionCycle.setIcon(icon3)
        self.actionCycle.setObjectName(_fromUtf8("actionCycle"))
        self.actionMakeClique = QtGui.QAction(GraphViewer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakeClique.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakeClique.setIcon(icon8)
        self.actionMakeClique.setObjectName(_fromUtf8("actionMakeClique"))
        self.actionMakeCycle = QtGui.QAction(GraphViewer)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakeCycle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakeCycle.setIcon(icon9)
        self.actionMakeCycle.setObjectName(_fromUtf8("actionMakeCycle"))
        self.actionMakePath = QtGui.QAction(GraphViewer)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/MakePath.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakePath.setIcon(icon10)
        self.actionMakePath.setObjectName(_fromUtf8("actionMakePath"))
        self.actionPath = QtGui.QAction(GraphViewer)
        self.actionPath.setCheckable(True)
        self.actionPath.setIcon(icon4)
        self.actionPath.setObjectName(_fromUtf8("actionPath"))
        self.actionRemoveAll = QtGui.QAction(GraphViewer)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RemoveAll.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveAll.setIcon(icon11)
        self.actionRemoveAll.setObjectName(_fromUtf8("actionRemoveAll"))
        self.actionRemoveEdges = QtGui.QAction(GraphViewer)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RemoveEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveEdges.setIcon(icon12)
        self.actionRemoveEdges.setObjectName(_fromUtf8("actionRemoveEdges"))
        self.actionSwapEdges = QtGui.QAction(GraphViewer)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/SwapEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSwapEdges.setIcon(icon13)
        self.actionSwapEdges.setObjectName(_fromUtf8("actionSwapEdges"))
        self.actionCompleteEdges = QtGui.QAction(GraphViewer)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/CompleteEdges.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompleteEdges.setIcon(icon14)
        self.actionCompleteEdges.setObjectName(_fromUtf8("actionCompleteEdges"))
        self.actionLeftBipartite = QtGui.QAction(GraphViewer)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/LeftBipartite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeftBipartite.setIcon(icon15)
        self.actionLeftBipartite.setObjectName(_fromUtf8("actionLeftBipartite"))
        self.actionCompleteBipartite = QtGui.QAction(GraphViewer)
        self.actionCompleteBipartite.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/RightBipartite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompleteBipartite.setIcon(icon16)
        self.actionCompleteBipartite.setObjectName(_fromUtf8("actionCompleteBipartite"))
        self.actionInsertGrid = QtGui.QAction(GraphViewer)
        self.actionInsertGrid.setIcon(icon6)
        self.actionInsertGrid.setObjectName(_fromUtf8("actionInsertGrid"))
        self.actionInsertClique = QtGui.QAction(GraphViewer)
        self.actionInsertClique.setIcon(icon2)
        self.actionInsertClique.setObjectName(_fromUtf8("actionInsertClique"))
        self.actionInsertCycle = QtGui.QAction(GraphViewer)
        self.actionInsertCycle.setIcon(icon3)
        self.actionInsertCycle.setObjectName(_fromUtf8("actionInsertCycle"))
        self.actionInsertPath = QtGui.QAction(GraphViewer)
        self.actionInsertPath.setIcon(icon4)
        self.actionInsertPath.setObjectName(_fromUtf8("actionInsertPath"))
        self.actionInsertBipartite = QtGui.QAction(GraphViewer)
        self.actionInsertBipartite.setIcon(icon7)
        self.actionInsertBipartite.setObjectName(_fromUtf8("actionInsertBipartite"))
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
        self.menuInsert.addAction(self.actionInsertGrid)
        self.menuInsert.addAction(self.actionInsertClique)
        self.menuInsert.addAction(self.actionInsertCycle)
        self.menuInsert.addAction(self.actionInsertPath)
        self.menuInsert.addAction(self.actionInsertBipartite)
        self.menuInsert.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.toolBar.addAction(self.actionSelection)
        self.toolBar.addAction(self.actionCreation)
        self.toolBar.addAction(self.actionClique)
        self.toolBar.addAction(self.actionCycle)
        self.toolBar.addAction(self.actionPath)
        self.toolBar.addAction(self.actionMove)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMakeClique)
        self.toolBar.addAction(self.actionMakeCycle)
        self.toolBar.addAction(self.actionMakePath)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLeftBipartite)
        self.toolBar.addAction(self.actionCompleteBipartite)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRemoveAll)
        self.toolBar.addAction(self.actionRemoveEdges)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSwapEdges)
        self.toolBar.addAction(self.actionCompleteEdges)
        self.toolBar.addSeparator()

        self.retranslateUi(GraphViewer)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(6)
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
        QtCore.QObject.connect(self.btnInsertBipartite, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionInsertBipartite.trigger)
        QtCore.QObject.connect(self.btnInsertClique, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionInsertClique.trigger)
        QtCore.QObject.connect(self.btnInsertCycle, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionInsertCycle.trigger)
        QtCore.QObject.connect(self.btnInsertGrid, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionInsertGrid.trigger)
        QtCore.QObject.connect(self.btnInsertPath, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionInsertPath.trigger)
        QtCore.QMetaObject.connectSlotsByName(GraphViewer)

    def retranslateUi(self, GraphViewer):
        GraphViewer.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("GraphViewer", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTransform.setTitle(QtGui.QApplication.translate("GraphViewer", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert.setTitle(QtGui.QApplication.translate("GraphViewer", "&Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.toolbox.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
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
        self.btnInsertGrid.setText(QtGui.QApplication.translate("GraphViewer", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertGrid.setDescription(QtGui.QApplication.translate("GraphViewer", "Inserts an N x M grid of nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertClique.setText(QtGui.QApplication.translate("GraphViewer", "Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertClique.setDescription(QtGui.QApplication.translate("GraphViewer", "Inserts a Kn clique", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertCycle.setText(QtGui.QApplication.translate("GraphViewer", "Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertCycle.setDescription(QtGui.QApplication.translate("GraphViewer", "Inserts a Cn cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertPath.setText(QtGui.QApplication.translate("GraphViewer", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertPath.setDescription(QtGui.QApplication.translate("GraphViewer", "Inserts an N nodes path", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Bipartite", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsertBipartite.setDescription(QtGui.QApplication.translate("GraphViewer", "Inserts an N x M bipartite graph", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageBasic), QtGui.QApplication.translate("GraphViewer", "Basic Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageCustomGraphs), QtGui.QApplication.translate("GraphViewer", "Custom Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setText(QtGui.QApplication.translate("GraphViewer", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to select several nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreation.setText(QtGui.QApplication.translate("GraphViewer", "Add Node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreation.setToolTip(QtGui.QApplication.translate("GraphViewer", "Adds a new node with double click", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("GraphViewer", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("GraphViewer", "Exit the graph creation tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("GraphViewer", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setText(QtGui.QApplication.translate("GraphViewer", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to drag the scene to move", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClique.setText(QtGui.QApplication.translate("GraphViewer", "Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClique.setToolTip(QtGui.QApplication.translate("GraphViewer", "New nodes will make a clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCycle.setText(QtGui.QApplication.translate("GraphViewer", "Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeClique.setText(QtGui.QApplication.translate("GraphViewer", "Make Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeClique.setToolTip(QtGui.QApplication.translate("GraphViewer", "Converts all the nodes in an clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeCycle.setText(QtGui.QApplication.translate("GraphViewer", "Make Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakeCycle.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a cycle between all selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakePath.setText(QtGui.QApplication.translate("GraphViewer", "Make Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMakePath.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a path between all selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPath.setText(QtGui.QApplication.translate("GraphViewer", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPath.setToolTip(QtGui.QApplication.translate("GraphViewer", "Allows to build a path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setText(QtGui.QApplication.translate("GraphViewer", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveAll.setToolTip(QtGui.QApplication.translate("GraphViewer", "Deletes all nodes selected and all related edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveEdges.setText(QtGui.QApplication.translate("GraphViewer", "Remove Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Deletes all edges between any pair of selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwapEdges.setText(QtGui.QApplication.translate("GraphViewer", "Swap Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwapEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Swaps all the edges between selected nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteEdges.setText(QtGui.QApplication.translate("GraphViewer", "Complete Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteEdges.setToolTip(QtGui.QApplication.translate("GraphViewer", "Adds the symetric edge for all edges between the nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeftBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Select Left Bipartite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeftBipartite.setToolTip(QtGui.QApplication.translate("GraphViewer", "Mark the selected nodes to be used later for a bipartite graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Complete Bipartite", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompleteBipartite.setToolTip(QtGui.QApplication.translate("GraphViewer", "Makes a bipartite graph with the currently selected and the previously selected ones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertGrid.setText(QtGui.QApplication.translate("GraphViewer", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertGrid.setToolTip(QtGui.QApplication.translate("GraphViewer", "Inserts an N x M grid of nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertClique.setText(QtGui.QApplication.translate("GraphViewer", "Clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertClique.setToolTip(QtGui.QApplication.translate("GraphViewer", "Inserts a Kn clique", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertCycle.setText(QtGui.QApplication.translate("GraphViewer", "Cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertCycle.setToolTip(QtGui.QApplication.translate("GraphViewer", "Inserts a Cn cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertPath.setText(QtGui.QApplication.translate("GraphViewer", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertPath.setToolTip(QtGui.QApplication.translate("GraphViewer", "Inserts an N nodes path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertBipartite.setText(QtGui.QApplication.translate("GraphViewer", "Bipartite Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertBipartite.setToolTip(QtGui.QApplication.translate("GraphViewer", "Inserts an N x M bipartite graph", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PropertyViewer.ui'
#
# Created: Sun May 20 00:36:24 2012
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
