__author__ = 'David'

import random as rdm
from node import Node
from copy import copy, deepcopy
import events as ev

class Behavior:

    #receiving data
    @staticmethod
    def Process(self, globalData, actualData, newData):pass
    @staticmethod
    def Learn(self, new):pass
    #sending data
    @staticmethod
    def Route(self, node): return []
    @staticmethod
    def Select(self, destination, data, actTime):return []
    @staticmethod
    def Transform(self, key, value):return value
    @staticmethod
    def Cleanup(self, data):pass
    #signaling
    @staticmethod
    def OnSignal(self, node, signalData, actualTime): return []

    def __init__(self):
        #sending
        self.sendAfterReceive = False
        self.includeBehavior = False
        #description
        self.Name = "None"
        #receiving data
        self.Process = Behavior.Process
        self.Learn = Behavior.Learn
        #sending data
        self.Route = Behavior.Route
        self.Select = Behavior.Select
        self.Transform = Behavior.Transform
        self.Cleanup = Behavior.Cleanup
        #signaling
        self.OnSignal = Behavior.OnSignal

    def __str__(self):
        return self.Name

    def __repr__(self):
        return self.Name

    def Clone(self):
        return copy(self)

class AttributedBehavior(Behavior):
    def __init__(self):
        super().__init__()
        self.attributesToAdd

class BasicProcessing:

    @staticmethod
    def UpdateAll():
        def UpdateAll(self,gloabalData,actualData,newData):
            actualData.update(newData)
        return UpdateAll

    @staticmethod
    def Update(keys):
        def UpdateOnly(self,gloabalData,actualData,newData):
            for k in keys:
                if k in newData: actualData[k] = newData[k]
        return UpdateOnly

    @staticmethod
    def ProbUpdate(dict):
        def ProbUpd(self,globalData, actualData,newData):
            for k,v in dict.items():
                if k in newData and rdm.random()<=v: actualData[k] = newData[k]
        return ProbUpd

class BasicLearning:

    @staticmethod
    def LearnAll():
        def LearnAll(self,new):
            self.sendAfterReceive = new.sendAfterReceive
            self.includeBehavior = new.includeBehavior
            self.Process = new.Process
            self.Learn = new.Learn
            self.Route = new.Route
            self.Select = new.Select
            self.Transform = new.Transform
            self.Cleanup = new.Cleanup
            self.OnSignal = new.OnSignal
        return LearnAll

    @staticmethod
    def LearnSpecificBehavior(sendAftReceive = False,sendBeh = False,process = False,learn = False,route = False,select = False,transform = False,cleanup = False,signaling = False):
        def LearnSpecific(self,new):
            if sendAftReceive: self.sendAfterReceive = new.sendAfterReceive
            if sendBeh: self.includeBehavior = new.includeBehavior
            if process: self.Process = new.Process
            if learn: self.Learn = new.Learn
            if route: self.Route = new.Route
            if select: self.Select = new.Select
            if transform: self.Transform = new.Transform
            if cleanup: self.Cleanup = new.Cleanup
            if signaling: self.OnSignal = new.OnSignal
        return LearnSpecific

    @staticmethod
    def LearnSendBehavior():
        return BasicLearning.LearnSpecificBehavior(sendAftReceive = True,sendBeh = True,route = True,select = True,transform = True)

    @staticmethod
    def LearnReceiveBehavior():
        return BasicLearning.LearnSpecificBehavior(process = True,learn = True)

class BasicRouting:

    @staticmethod
    def All():
        def AllDestinations(self,node):
            for s in node.Successors():
                yield s
        return AllDestinations

    @staticmethod
    def Sample(amount):
        def SampleDestinations(self,node):
            n= min(len(node.Successors()),amount)
            if n<=0: return []
            return rdm.sample(node.Successors(),n)
        return SampleDestinations

class BasicSelection:

    @staticmethod
    def AllAtOnce(timeFunction):
        def SendAllData(self,destination,data,actTime):
            yield (data.keys() , actTime + timeFunction())
        return SendAllData

    @staticmethod
    def OneByOne(timeFunction):
        def SendOneByOne(self,destination,data,actTime):
            for k in data.keys():
                yield ([k],actTime + timeFunction())
        return SendOneByOne

    @staticmethod
    def SpecificGroup(keys,timeFunction):
        def SendSelectedData(self,destination,data,actTime):
            r = []
            for k in keys:
                if k in data: r.append(k)
            yield (r,actTime+timeFunction())
        return SendSelectedData

class BasicTransformation:

    @staticmethod
    def ShallowCopy():
        def Shallow(self,key,value):
            return copy(value)
        return Shallow

    @staticmethod
    def DeepCopy():
        def Deep(self,key,value):
            return deepcopy(value)
        return Deep

class BasicCleanup:

    @staticmethod
    def Delete(keys):
        def DeleteSpecific(self,data):
            for item in [k for k in keys if k in data]:
                del data[item]
        return DeleteSpecific

    @staticmethod
    def DeleteAll(behavior = False):
        def DelAll(self,data):
            b = False
            if not behavior and Node.bkey in data: b = data.pop(Node.bkey)
            data.clear()
            if b: data[Node.bkey] = b
        return DelAll

class BasicSignaling:

    @staticmethod
    def SendOnSignal():
        def SendOnSignal(self, node, signalData, actTime):
            return node.SendData(actTime)
        return SendOnSignal

    @staticmethod
    def SendPeriodically(timeFunction):
        def SendPeriod(self, node, signalData,actTime):
            return list(node.SendData(actTime))+[ev.Signal(node,None,actTime+timeFunction())]
        return SendPeriod








