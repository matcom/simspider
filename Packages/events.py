__author__ = 'David'

import node

class Event:

    def __init__(self,time):
        self.time = time
        self.name = "Empty event"

    def Process(self): pass

    def __str__(self):
        return self.name + " in time: {0}.".format(self.time)

class SignalAllNodes(Event):

    def __init__(self, graph, signalData, time):
        super().__init__(time)
        self.graph = graph
        self.signalData = signalData
        self.name = "Signal all nodes"

    def Process(self):
        result = []
        for n in [node.Node(self.graph,nod) for nod in self.graph.nodes_iter()]:
            result += n.Signal(self.signalData,self.time)
        return result

class NodeEvent(Event):
    def __init__(self,time,node):
        super().__init__(time)
        self.node = node
        self.name = "Empty node event"

class DataArrival(NodeEvent):

    def __init__(self, source, data, node, time):
        super().__init__(time,node)
        self.data = data
        self.source = source
        self.name = "Data arrival to node {0}".format(self.node)

    def Process(self):
        return self.node.ReceiveData(self.source, self.data, self.time)

class DataDeparture(NodeEvent):

    def __init__(self,time,node):
        super().__init__(time,node)
        self.name = "Data departure from node {0}".format(self.node)

    def Process(self):
        return self.node.SendData(self.time)

class Signal(NodeEvent):

    def __init__(self, node, signalData, time):
        super().__init__(time,node)
        self.signalData = signalData
        self.name = "Node {0} signaled".format(self.node)

    def Process(self):
        return self.node.Signal(self.signalData, self.time)