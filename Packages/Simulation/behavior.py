__author__ = 'David'

import random as rdm
import node
from copy import copy, deepcopy
import events as ev
import fuzzybehavior as fb

class Behavior:

    def __init__(self):
        #sending
        self.sendAfterReceive = False
        self.includeBehavior = False
        #description
        self.name = "None"
        #owner
        self.node = None
        #common data
        self.commonData = None
        #receiving data
        object.__setattr__(self,'Process',type(self).Process)
        object.__setattr__(self,'Learn',type(self).Learn)
        #sending data
        object.__setattr__(self,'Route',type(self).Route)
        object.__setattr__(self,'Select',type(self).Select)
        object.__setattr__(self,'Transform',type(self).Transform)
        object.__setattr__(self,'Cleanup',type(self).Cleanup)
        #signaling
        object.__setattr__(self,'OnSignal',type(self).OnSignal)

    @staticmethod
    def __SetMethodAsField(instance,name):
        #instance.name = type(instance).name
        object.__setattr__(instance,name,object.__getattribute__(type(instance),name))

    #receiving data
    def Process(self, globalData, actualData, newData):pass
    def Learn(self, new):pass
    #sending data
    def Route(self, node): return []
    def Select(self, destination, data, actTime):return []
    def Transform(self, key, value):return value
    def Cleanup(self, nodeData):pass
    #signaling
    def OnSignal(self, node, signalData, actualTime): return []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def Clone(self):
        return copy(self)

class BasicProcessing:

    @staticmethod
    def UpdateAll():
        def UpdateAll(self,globalData,actualData,newData):
            actualData.update(newData)
        return UpdateAll

    @staticmethod
    def Update(keys):
        def UpdateOnly(self,globalData,actualData,newData):
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
            if isinstance(new,fb.FuzzyBehavior) and isinstance(self,fb.FuzzyBehavior):
                self.sendAfterReceive = new.sendAfterReceive
                self.includeBehavior = new.includeBehavior
                self.Learn = new.Learn
                self.Route = new.Route
                self.Select = new.Select
                self.Transform = new.Transform
                self.Cleanup = new.Cleanup
                self.OnSignal = new.OnSignal
                self.PreProcess = new.PreProcess
                self.UserDefinedProcess = new.UserDefinedProcess
                self.OutputVars.update(new.OutputVars)
                #self.Process = new.Process
            elif  isinstance(new,Behavior) and isinstance(self,Behavior):
                self.sendAfterReceive = new.sendAfterReceive
                self.includeBehavior = new.includeBehavior
                self.Learn = new.Learn
                self.Route = new.Route
                self.Select = new.Select
                self.Transform = new.Transform
                self.Cleanup = new.Cleanup
                self.OnSignal = new.OnSignal
                self.Process = new.Process
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

class BasicRouting:

    @staticmethod
    def All():
        def AllDestinations(self,node):
            for s in node.Successors():
                yield s
        return AllDestinations

    # TODO: Exception en random.sample: successors es un dictionary

    @staticmethod
    def Sample(amount):
        def SampleDestinations(self,node):
            n= min(len(list(node.Successors())),amount)
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
            if not behavior and node.Node.bkey in data: b = data.pop(node.Node.bkey)
            data.clear()
            if b: data[node.Node.bkey] = b
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








