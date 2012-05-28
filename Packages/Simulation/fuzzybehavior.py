__author__ = 'Claudia'
#import sys
#import os
#import Redist.Redist.pyfuzzy.System
import Redist.pyfuzzy.storage.fcl.Reader
import Packages.Simulation.behavior as b
from Redist.pyfuzzy.OutputVariable import OutputVariable
from Redist.pyfuzzy.InputVariable import InputVariable

class FuzzyBehavior(b.Behavior):
    def __init__(self,path = None, system = None):
        super().__init__()
        if path is None :
            self.__FuzzySystem = system
        else :
            self.__FuzzySystem = Redist.pyfuzzy.storage.fcl.Reader.Reader().load_from_file(path)
        self.ProcessFuzzyVar = {}
        self.CleanupFuzzyVar ={}
        self.LearnFuzzyVar={}
        self.RoutFuzzyVar = {}
        self.SelectFuzzyVar ={}
        self.TransformFuzzyVar = {}
        self.OnSignalFuzzyVar = {}
        self.__UserDefinedProcess=None

    def BoundToProcess(self,names):
        self.ProcessFuzzyVar = names

    def BoundToLearn(self,names):
        self.LearnFuzzyVar = names

    def BoundToRout(self,names):
        self.RoutFuzzyVar = names

    def BoundToSelect(self,names):
        self.SelectFuzzyVar = names

    def BoundToTransform(self,names):
        self.TransformFuzzyVar = names

    def BoundToCleanup(self,names):
        self.CleanupFuzzyVar = names

    def BoundToOnSignal(self,names):
        self.OnSignalFuzzyVar = names

#    def AddValuesToNode(self,list_var,node):
#        for name,value in self.FuzzySystem.variables.items():
#            node.SetAttribute(name,value)
#        return

    def Process(self,globalData,actualData,newData):
        input = {}
        output = {}
        for var in self.FuzzySystem.variables.items():
            key,value = var
            if value is OutputVariable:
                output.append(key,None)
            if value is InputVariable:
                ret,val = FuzzyBehavior.SearchVariable(key,globalData,actualData,newData)
                if ret:
                    input.append(key,val)
        self.FuzzySystem.calculate(input,output)
        for i in output.items():
            key,value = i
            if self.ProcessFuzzyVar.contains(key): self.ProcessFuzzyVar[key] = value
            if self.CleanupFuzzyVar.contains(key): self.CleanupFuzzyVar[key] = value
            if self.TransformFuzzyVar.contains(key): self.TransformFuzzyVar[key] = value
            if self.SelectFuzzyVar.contains(key): self.SelectFuzzyVar[key] = value
            if self.LearnFuzzyVar.contains(key): self.LearnFuzzyVar[key] = value
            if self.RoutFuzzyVar.contains(key): self.RoutFuzzyVar[key] = value
            if self.OnSignalFuzzyVar.contains(key): self.OnSignalFuzzyVar[key] = value
            for key in output:
                if actualData.contains(key):
                    actualData[key]=output[key]
        self.__UserDefinedProcess(self,globalData,actualData,newData)


    def __setattr__(self, key, value):
        if key == 'Process':
            object.__setattr__(self,'__UserDefinedProcess', value)
        else:
            super().__setattr__(key,value)


    @staticmethod
    def SearchVariable(key,globalData,actualData,newData):
        if actualData.contains(key):
            return (True,actualData[key])
        if newData.contains(key):
            return (True , newData[key])
        if globalData.contains[key]:
            return (True,globalData[key])
        return (False , 0)