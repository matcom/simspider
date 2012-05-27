__author__ = 'David'

from node import Node

def RegisterTracker(tracker):
    Node.trackers.append(tracker)

def ClearAllTrackers():
    Node.trackers = []

class Tracker:

    def __init__(self,nodes = None):
        if nodes!=None: self.__nodes = set(nodes)
        else: self.__nodes = None

    def NodeSignaled(self, node, signalData, time): pass

    def DataReceived(self, node, receivedData, source, time): pass

    def DataSent(self, node, data, destination, time, arrival): pass

    def DataUpdated(self,node): pass

    def DataCleaned(self,node): pass

    def IsTracked(self,node):
        if not self.__nodes: return True
        else: return node.node in self.__nodes

class NodeLog(Tracker):

    def NodeSignaled(self, node, signalData, time):
        if self.IsTracked(node):
            print("Node {0} was signaled with data: {1} time: {2}".format(node,signalData,time))

    def DataReceived(self, node, receivedData, source, time):
        if self.IsTracked(node):
            print("Time: {0}".format(time))
            print("Node {0} received: {1} from {2}".format(node,receivedData,source))
            print("Actual data in node {0}: {1}".format(node,node.GetData()))
            print("Actual global data: {0}".format(node.GetGlobalData()))

    def DataSent(self, node, data, destination, time, arrival):
        if self.IsTracked(node):
            print("Sending: {0} from {1} to {2} delay: {3}".format(data, node, destination, arrival - time))

    def DataUpdated(self,node):
        if self.IsTracked(node):
            print("Processed data in node {0}: {1}".format(node,node.GetData()))

    def DataCleaned(self,node):
        if self.IsTracked(node):
            print("Data after cleanup in node {0}: {1}".format(node, node.GetData()))

class EdgeLog(Tracker):

    def DataSent(self, node, data, destination, time, arrival):
        if self.IsTracked(node)or self.IsTracked(destination):
            print("Edge {0} is passing {1} delay {2}".format((node.node,destination.node),data,arrival-time))

class AttributeTracker(Tracker):

    def __init__(self, attributes):
        super().__init__()
        self.attributesPath = dict(zip(attributes,[set() for n in range(len(attributes))]))

    def DataSent(self, node, data, destination, time, arrival):
        for a in self.attributesPath:
            if a in data:
                self.attributesPath[a].add((node,destination))




