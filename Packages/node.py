# -*- coding: utf8 -*-
__author__ = 'David'

import behavior as be
import events as ev
import debug

class Node:

    dkey = "__data__"
    bkey = "behavior"

    def __init__(self,graph,node):
        self.graph = graph
        self.node = node
        if Node.dkey not in self.graph.node[node]: graph.node[node][Node.dkey] = {}
        data = graph.node[node][Node.dkey]
        if Node.bkey not in data: data[Node.bkey] = be.Behavior()

    def ReceiveData(self, source, newData, actTime):
        d = self.GetData()
        print("Time: {0}".format(actTime))
        print("Node {0} received: {1}".format(self,newData))
        print("Actual data in node {0}: {1}".format(self,d))
        print("Actual data in graph: {1}".format(self,self.graph.graph))
        newbeh = False
        b = self.GetBehavior()
        if Node.bkey in newData: newbeh = newData.pop(Node.bkey)
        b.Process(b, self.graph.graph, d, newData)
        if newbeh: b.Learn(b,newbeh)
        print("Updated data in node {0}: {1}".format(self,d))
        if b.sendAfterReceive: return self.SendData(actTime)
        else: return []

    def SendData(self, actTime):
        newEvents = []
        b = self.GetBehavior()
        data = self.GetData()
        if len(data)>0:
            for d in [Node(self.graph, d) for d in b.Rout(b,self)]:
                if not b.includeBehavior: del data[Node.bkey]
                for ks, time in b.Select(b, data, actTime):
                    newData = {}
                    for key in ks:
                        newData[key] = b.Transform(b, key, data[key])
                    newEvents.append(ev.DataArrival(self, newData, d, time))
                    print("Sending: {0} from {1} to {2} time: {3}".format(newData, self, d, actTime))
                    print("will arrive in time {0}".format(time))
            b.Cleanup(b, data)
            print("Data after cleanup in node {0}: {1}".format(self, data))
            if Node.bkey not in data: data[Node.bkey] = b
        return newEvents

    def Signal(self, signalData, actTime):
        print("Node {0} was signaled with data: {1} time: {2}".format(self,signalData,actTime))
        b = self.GetBehavior()
        return b.OnSignal(b, self, signalData,actTime)

    def GetData(self):
        return self.graph.node[self.node][Node.dkey]

    def SetAttribute(self,key,value):
        if key==Node.bkey: raise Exception("The key \""+Node.bkey+"\" is used to store the node behavior.")
        self.GetData()[key] = value

    def GetAttribute(self,key):
        return self.GetData()[key]

    def __getitem__(self, item):
        return self.GetAttribute(item)

    def __setitem__(self, key, value):
        self.SetAttribute(key,value)

    def Attributes(self):
        for k,v in self.GetData().items():
            if k!=Node.bkey: yield (k,v)

    def SetBehavior(self,b):
        self.GetData()[Node.bkey] = b
        if isinstance(b,be.AttributedBehavior):
            for k,v in b.attributesToAdd.items():
                self[k]=v

    def GetBehavior(self):
        return self.GetData()[Node.bkey]

    def Successors(self):
        return self.graph.successors(self.node)

    def __str__(self):
        return str(self.node)
