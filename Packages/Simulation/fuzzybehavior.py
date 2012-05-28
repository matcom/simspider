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
        for i in names:
            self.ProcessFuzzyVar[i] =None

    def BoundToLearn(self,names):
        for i in names:
            self.LearnFuzzyVar[i] =None

    def BoundToRout(self,names):
        for i in names:
            self.RoutFuzzyVar[i] =None

    def BoundToSelect(self,names):
        for i in names:
            self.SelectFuzzyVar[i] =None

    def BoundToTransform(self,names):
        for i in names:
            self.TransformFuzzyVar[i] =None

    def BoundToCleanup(self,names):
        for i in names:
            self.CleanupFuzzyVar[i] =None

 #   def BoundToOnSignal(self,names):
#        self.OnSignalFuzzyVar = names

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

    @staticmethod
    def Sample():
        def SampleDestinations(self,node):
            happiness_value = self.RoutFuzzyVar['Happiness']
            if happiness_value is None:
                happiness_value = 0
                print('No se computo el sistema fuzzy')
            n=0
            for i in node.Successors():
                n = n +1
            n = n*happiness_value/10
            if n<=0: return []
            return n
        return SampleDestinations

    @staticmethod
    def Process_Opt():
        def ProcessOpt(self,globalData,actualData,newData):
            values = self.ProcessFuzzyVar
            for key in actualData:
                if not key in values and key in newData:
                    actualData[key] = newData[key]
        return ProcessOpt

    @staticmethod
    def SpecificGroup(keys,timeFunction):
        def SendSelectedData(self,destination,data,actTime):
            r = []
            for k in keys:
                if k in data: r.append(k)
            yield (r,actTime+timeFunction())
        return SendSelectedData
