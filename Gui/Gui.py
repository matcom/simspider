# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GraphViewer.ui'
#
# Created: Sat May 19 10:07:02 2012
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
        GraphViewer.resize(655, 486)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GraphViewer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GraphViewer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GraphViewer.setStatusBar(self.statusbar)
        self.toolbox = QtGui.QDockWidget(GraphViewer)
        self.toolbox.setObjectName(_fromUtf8("toolbox"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.pageDesign = QtGui.QWidget()
        self.pageDesign.setGeometry(QtCore.QRect(0, 0, 145, 317))
        self.pageDesign.setObjectName(_fromUtf8("pageDesign"))
        self.toolBox.addItem(self.pageDesign, _fromUtf8(""))
        self.pageGraphs = QtGui.QWidget()
        self.pageGraphs.setGeometry(QtCore.QRect(0, 0, 145, 317))
        self.pageGraphs.setObjectName(_fromUtf8("pageGraphs"))
        self.toolBox.addItem(self.pageGraphs, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBox)
        self.toolbox.setWidget(self.dockWidgetContents)
        GraphViewer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolbox)
        self.toolBar = QtGui.QToolBar(GraphViewer)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        GraphViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelection = QtGui.QAction(GraphViewer)
        self.actionSelection.setCheckable(True)
        self.actionSelection.setChecked(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelection.setIcon(icon)
        self.actionSelection.setObjectName(_fromUtf8("actionSelection"))
        self.toolBar.addAction(self.actionSelection)

        self.retranslateUi(GraphViewer)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GraphViewer)

    def retranslateUi(self, GraphViewer):
        GraphViewer.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolbox.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageDesign), QtGui.QApplication.translate("GraphViewer", "Design", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageGraphs), QtGui.QApplication.translate("GraphViewer", "Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("GraphViewer", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelection.setText(QtGui.QApplication.translate("GraphViewer", "Selection", None, QtGui.QApplication.UnicodeUTF8))

