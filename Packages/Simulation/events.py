__author__ = 'David'

import node

class Event:

    def __init__(self,time):
        self.time = time
        self.name = "Empty event"

    def Process(self): pass

    def __str__(self):
        return self.name + " in time: {0}.".format(self.time)

    def __lt__(self, other):
        return self.time.__lt__(other.time)

    def __eq__(self, other):
        return self.time.__eq__(other.time)

    def __gt__(self, other):
        return self.time.__gt__(other.time)

    def __ge__(self, other):
        return self.time.__ge__(other.time)

    def __le__(self, other):
        return self.time.__le__(other.time)

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

class GraphEvent(Event):

    def __init__(self, time, graph):
        super().__init__(time)
        self.graph = graph
        self.name = "Graph event"

class PeriodicalGraphEvent(GraphEvent):

    def __init__(self, time, graph, timeFunction,  processData):
        super().__init__(time, graph)
        self.timeFunction = timeFunction
        self.processData = processData
        self.name = "Custom periodical graph event"

    def Process(self):
        self.processData(self.graph.graph)
        self.time += self.timeFunction()
        return [self]

class NodeEvent(Event):

    def __init__(self, time, node):
        super().__init__(time)
        self.node = node
        self.name = "Node event"

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