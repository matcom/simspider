__author__ = 'David'

import node

class Event:

    def __init__(self,time):
        self.time = time

    def Process(self): pass

    def __str__(self):
        return "(time-> {0})".format(self.time)

class DataArrival(Event):

    def __init__(self, source, data, destination, time):
        super().__init__(time)
        self.data = data
        self.source = source
        self.destination = destination

    def Process(self):
        return self.destination.ReceiveData(self.source, self.data, self.time)

class DataDeparture(Event):

    def __init__(self, source, time):
        super().__init__(time)
        self.source = source

    def Process(self):
        return self.source.SendData(self.time)

class Signal(Event):

    def __init__(self, destination, signalData, time):
        super().__init__(time)
        self.destination = destination
        self.signalData = signalData

    def Process(self):
        return self.destination.Signal(self.signalData, self.time)

class SignalAllNodes(Event):

    def __init__(self, graph, signalData, time):
        super().__init__(time)
        self.graph = graph
        self.signalData = signalData

    def Process(self):
        result = []
        for n in [node.Node(self.graph,nod) for nod in self.graph.nodes_iter()]:
            result += n.Signal(self.signalData,self.time)
        return result
