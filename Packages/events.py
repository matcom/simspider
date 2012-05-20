# -*- coding: utf8 -*-

__author__ = 'David'

import node

class Event:

    def __init__(self,time):
        self.time = time

    def process(self): pass

    def __str__(self):
        return "(time-> {0})".format(self.time)

class DataArrival(Event):

    def __init__(self, source, data, destination, time):
        super().__init__(time)
        self.data = data
        self.source = source
        self.destination = destination

    def process(self):
        try:
            result = self.destination.ReceiveData(self.source, self.data, self.time)
        except Exception as ex:
            print(ex)
            result = []
        return result

class DataDeparture(Event):

    def __init__(self, source, time):
        super().__init__(time)
        self.source = source

    def process(self):
        try:
            result = self.source.SendData(self.time)
        except Exception as ex:
            print(ex)
            result = []
        return result

class Signal(Event):

    def __init__(self, destination, signalData, time):
        super().__init__(time)
        self.destination = destination
        self.signalData = signalData

    def process(self):
        try:
            result = self.destination.Signal(self.signalData, self.time)
        except Exception as ex:
            print(ex)
            result = []
        return result

class SignalAllNodes(Event):

    def __init__(self, graph, signalData, time):
        super().__init__(time)
        self.graph = graph
        self.signalData = signalData

    def process(self):
        result = []
        for n in [node.Node(self.graph,nod) for nod in self.graph.nodes_iter()]:
            try:
                result += n.Signal(self.signalData,self.time)
            except Exception as ex:
                print(ex)
        return result
