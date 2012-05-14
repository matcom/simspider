__author__ = 'David'

import random as rdm
from node import Node
from copy import copy, deepcopy
import events as ev

class Behavior:

    def __init__(self):
        #receiving data
        self.Process = None
        self.Learn = None
        #sending data
        self.sendAfterReceive = False
        self.includeBehavior = False
        self.Rout = None
        self.Select = None
        self.Transform = None
        self.Cleanup = None
        #signaling
        self.OnSignal = None
        #description
        self.Name = "None"

    def __str__(self):
        return self.Name

    def __repr__(self):
        return self.Name

class BasicProcessing:

    @staticmethod
    def UpdateAll():
        def UpdateAll(actualData,newData):
            actualData.update(newData)
        return UpdateAll

    @staticmethod
    def DoNothing():
        return None

    @staticmethod
    def Update(keys):
        def UpdateOnly(actualData,newData):
            for k in keys:
                if k in newData: actualData[k] = newData[k]
        return UpdateOnly

    @staticmethod
    def ProbUpdate(dict):
        def ProbUpd(actualData,newData):
            for k,v in dict.items():
                if k in newData and rdm.random()<=v: actualData[k] = newData[k]
        return ProbUpd

class BasicLearning:

    @staticmethod
    def LearnAll():
        def LearnAll(actual,new):
            actual.sendAfterReceive = new.sendAfterReceive
            actual.includeBehavior = new.includeBehavior
            actual.Process = new.Process
            actual.Learn = new.Learn
            actual.Rout = new.Rout
            actual.Select = new.Select
            actual.Transform = new.Transform
            actual.Cleanup = new.Cleanup
            actual.OnSignal = new.OnSignal
        return LearnAll

    @staticmethod
    def DoNothing():
        return None

    @staticmethod
    def LearnSpecificBehavior(sendAftReceive = False,sendBeh = False,process = False,learn = False,rout = False,select = False,transform = False,cleanup = False,signaling = False):
        def LearnSpecific(actual,new):
            if sendAftReceive: actual.sendAfterReceive = new.sendAfterReceive
            if sendBeh: actual.includeBehavior = new.includeBehavior
            if process: actual.Process = new.Process
            if learn: actual.Learn = new.Learn
            if rout: actual.Rout = new.Rout
            if select: actual.Select = new.Select
            if transform: actual.Transform = new.Transform
            if cleanup: actual.Cleanup = new.Cleanup
            if signaling: actual.OnSignal = new.OnSignal
        return LearnSpecific

    @staticmethod
    def LearnSendBehavior():
        return BasicLearning.LearnSpecificBehavior(sendAftReceive = True,sendBeh = True,rout = True,select = True,transform = True)

    @staticmethod
    def LearnReceiveBehavior():
        return BasicLearning.LearnSpecificBehavior(process = True,learn = True)

class BasicRouting:

    @staticmethod
    def All():
        def AllDestinations(node):
            for s in node.Successors():
                yield s
        return AllDestinations

    @staticmethod
    def Sample(amount):
        def SampleDestinations(node):
            n= min(len(node.Successors()),amount)
            if n<=0: return []
            return rdm.sample(node.Successors(),n)
        return SampleDestinations

    @staticmethod
    def DoNothing():
        return None

class BasicSelection:

    @staticmethod
    def AllAtOnce(timeFunction):
        def SendAllData(data,actTime):
            yield (data.keys() , actTime + timeFunction())
        return SendAllData

    @staticmethod
    def OneByOne(timeFunction):
        def SendOneByOne(data,actTime):
            for k in data.keys():
                yield ([k],actTime + timeFunction())
        return SendOneByOne

    @staticmethod
    def SpecificGroup(keys,timeFunction):
        def SendSelectedData(data,actTime):
            r = []
            for k in keys:
                if k in data: r.append(k)
            yield (r,actTime+timeFunction())
        return SendSelectedData

    @staticmethod
    def DoNothing():
        return None

class BasicTransformation:

    @staticmethod
    def DoNothing():
        return None

    @staticmethod
    def ShallowCopy():
        def Shallow(key,value):
            return copy(value)
        return Shallow

    @staticmethod
    def DeepCopy():
        def Deep(key,value):
            return deepcopy(value)
        return Deep

class BasicCleanup:

    @staticmethod
    def DoNothing():
        return None

    @staticmethod
    def Delete(keys):
        def DeleteSpecific(data):
            for item in [k for k in keys if k in data]:
                del data[item]
        return DeleteSpecific

    @staticmethod
    def DeleteAll(behavior = False):
        def DelAll(data):
            b = False
            if not behavior and Node.bkey in data: b = data.pop(Node.bkey)
            data.clear()
            if b: data[Node.bkey] = b
        return DelAll

class BasicSignaling:

    @staticmethod
    def SendOnSignal():
        def SendOnSignal(node, signalData, actTime):
            return node.SendData(actTime)
        return SendOnSignal

    @staticmethod
    def SendPeriodically(timeFunction):
        def SendPeriod(node, signalData,actTime):
            return list(node.SendData(actTime))+[ev.Signal(node,None,actTime+timeFunction())]
        return SendPeriod








