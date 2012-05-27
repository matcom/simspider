# -*- coding: utf8 -*-
__author__ = 'David'

import behavior as be
import events as ev
import debug

class Node:

    dkey = "__data__"
    bkey = "behavior"
    trackers = []

    def __init__(self,graph,node):
        self.graph = graph
        self.node = node
        if Node.dkey not in self.graph.node[node]: graph.node[node][Node.dkey] = {}
        data = graph.node[node][Node.dkey]
        if Node.bkey not in data: data[Node.bkey] = be.Behavior()

    def ReceiveData(self, source, newData, actTime):
        d = self.GetData()
        b = self.GetBehavior()
        for nt in Node.trackers:
            nt.DataReceived(self,newData,source,actTime)
        newbeh = False
        if Node.bkey in newData: newbeh = newData.pop(Node.bkey)
        b.Process(b, self.GetGlobalData(), d, newData)
        if newbeh: b.Learn(b,newbeh)
        for nt in Node.trackers:
            nt.DataUpdated(self)
        if b.sendAfterReceive: return self.SendData(actTime)
        else: return []

    def SendData(self, actTime):
        newEvents = []
        b = self.GetBehavior()
        data = self.GetData()
        if len(data)>0:
            if not b.includeBehavior: del data[Node.bkey]
            for d in b.Route(b,self):
                #if not isinstance(d,Node): d = Node(self.graph,d)
                for ks, time in b.Select(b, d, data, actTime):
                    newData = {}
                    for key in ks:
                        newData[key] = b.Transform(b, key, data[key])
                    newEvents.append(ev.DataArrival(self, newData, d, time))
                    for nt in Node.trackers:
                        nt.DataSent(self,newData,d,actTime,time)
            b.Cleanup(b, data)
            for nt in Node.trackers:
                nt.DataCleaned(self)
            if Node.bkey not in data: data[Node.bkey] = b
        return newEvents

    def Signal(self, signalData, actTime):
        for nt in Node.trackers:
            nt.NodeSignaled(self,signalData,actTime)
        b = self.GetBehavior()
        return b.OnSignal(b, self, signalData,actTime)

    def GetData(self):
        return self.graph.node[self.node][Node.dkey]

    def GetGlobalData(self):
        return self.graph.graph

    def SetAttribute(self,key,value):
        if key==Node.bkey: raise Exception("The key \""+Node.bkey+"\" is used to store the node behavior.")
        self.GetData()[key] = value

    def HasAttribute(self,attribute):
        return attribute in self.GetData()

    def GetAttribute(self,key):
        return self.GetData()[key]

    def Attributes(self,inclBehavior=False):
        for k in self.GetData():
            if inclBehavior or k!=Node.bkey: yield k

    def SetBehavior(self, b):
        self.GetData()[Node.bkey] = b
        b.node = self

    def GetBehavior(self):
        return self.GetData()[Node.bkey]

    def Successors(self):
        for n in [Node(self.graph,node) for node in self.graph.successors(self.node)]:
            yield n

    def __hash__(self):
        return self.node.__hash__()

    def __lt__(self, other):
        return self.node < other.node

    def __eq__(self, other):
        return self.node == other.node

    def __gt__(self, other):
        return self.node > other.node

    def __ge__(self, other):
        return self.node >= other.node

    def __le__(self, other):
        return self.node <= other.node

    def __getitem__(self, item):
        return self.GetAttribute(item)

    def __setitem__(self, key, value):
        self.SetAttribute(key,value)

    def __str__(self):
        return str(self.node)

