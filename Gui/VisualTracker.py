# -*- coding: utf8 -*-

from Simulation.gathering import Tracker

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import debug


class VisualTracker(Tracker):
    def __init__(self, graphViewer):
        super().__init__()
        self.graphViewer = graphViewer

    def NodeSignaled(self, node, signalData, time):
        if self.IsTracked(node):
            debug.info("Node {0} was signaled with data: {1} time: {2}", (node,signalData,time), "log")
            node.node.pen.setColor(Qt.yellow)
            self.graphViewer.ui.graphicsView.update()

    def DataReceived(self, node, receivedData, source, time):
        if self.IsTracked(node):
            debug.info("Time: {0}", (time,), "log")
            debug.info("Node {0} received: {1} from {2}", (node,receivedData,source), "log")
            debug.info("Actual data in node {0}: {1}", (node,node.GetData()), "log")
            debug.info("Actual global data: {0}", (node.GetGlobalData(),), "log")
            node.node.pen.setColor(Qt.green)
            self.graphViewer.ui.graphicsView.update()

    def DataSent(self, node, data, destination, time, arrival):
        if self.IsTracked(node):
            debug.info("Sending: {0} from {1} to {2} delay: {3}", (data, node, destination, arrival - time), "log")
            node.node.pen.setColor(Qt.red)
            self.graphViewer.ui.graphicsView.update()

    def DataUpdated(self,node):
        if self.IsTracked(node):
            debug.info("Processed data in node {0}: {1}", (node,node.GetData()), "log")

    def DataCleaned(self,node):
        if self.IsTracked(node):
            debug.info("Data after cleanup in node {0}: {1}", (node, node.GetData()), "log")
