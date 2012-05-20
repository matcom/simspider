# -*- coding: utf8 -*-

__author__ = 'David'

import behavior as beh
import events as ev

class Node:

    dkey = "__data__"
    bkey = "__beha__"

    def __init__(self,graph,node):
        self.graph = graph
        self.node = node
        if Node.dkey not in self.graph.node[node]: graph.node[node][Node.dkey] = {}
        self.data = graph.node[node][Node.dkey]
        if Node.bkey not in self.data: self.data[Node.bkey] = beh.Behavior()

    def ReceiveData(self, source, newData, actTime):
        print("Time: {0}".format(actTime))
        print("Received in {0} data: {1}".format(self,newData))
        print("Actual data in {0}: {1}".format(self,self.data))
        newbeh = False
        b = self.GetBehavior()
        if Node.bkey in newData: newbeh = newData.pop(Node.bkey)
        if b.Process != None: b.Process(self.data,newData)
        if b.Learn != None and newbeh: b.Learn(b,newbeh)
        print("Updated data in {0}: {1}".format(self,self.data))
        if b.sendAfterReceive: return self.SendData(actTime)
        else: return []

    def SendData(self, actTime):
        newEvents = []
        b = self.GetBehavior()
        if b.Rout != None and len(self.data)>0 and b.Select != None:
            for d in [Node(self.graph,d) for d in b.Rout(self)]:
                if not b.includeBehavior: del self.data[Node.bkey]
                for ks, time in b.Select(self.data, actTime):
                    newData = {}
                    for key in ks:
                        if b.Transform == None :
                            newData[key] = self.data[key]
                        else:
                            newData[key] = b.Transform(key,self.data[key])
                    newEvents.append(ev.DataArrival(self,newData,d,time))
                    print("Sending: {0} from: {1} to: {2} time: {3}".format(newData,self,d,actTime))
                if b.Cleanup != None: b.Cleanup(self.data)
                print("Data after cleanup in {0}: {1}".format(self,self.data))
                if not b.includeBehavior: self.data[Node.bkey] = b
        return newEvents

    def Signal(self, signalData, actTime):
        print("Node {0} was signaled with data: {1} time: {2}".format(self,signalData,actTime))
        b = self.GetBehavior()
        if b.OnSignal != None: return b.OnSignal(self, signalData,actTime)
        else: return []

    def SetAttribute(self,key,value):
        self.data[key] = value

    def GetAttribute(self,key):
        return self.data[key]

    def SetBehavior(self,b):
        self.data[Node.bkey] = b

    def GetBehavior(self):
        return self.data[Node.bkey]

    def Successors(self):
        return self.graph.successors(self.node)

    def __str__(self):
        return str(self.node)
