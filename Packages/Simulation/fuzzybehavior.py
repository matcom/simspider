__author__ = 'Claudia'
#import sys
#import os
#import Redist.Redist.pyfuzzy.System
import Redist.pyfuzzy.storage.fcl.Reader
import Packages.Simulation.behavior as b
from Redist.pyfuzzy.OutputVariable import OutputVariable
from Redist.pyfuzzy.InputVariable import InputVariable
import random as rdm

class FuzzyBehavior(b.Behavior):
    def __init__(self, system = None):
        super().__init__()
        object.__setattr__(self,'PreProcess',type(self).PreProcess)
        if system : self.SetSystem(system)
        def __EmptyProcess(self,globalData,actualData,newData): pass
        self.UserDefinedProcess = __EmptyProcess

    def SetSystem(self, system):
        self.__FuzzySystem = system
        self.OutputVars = {}
        for key,value in self.__FuzzySystem.variables.items():
            if isinstance(value,OutputVariable):
                self.OutputVars[key]=None

    def PreProcess(self,globalData,actualData,newData): pass

    def Process(self,globalData,actualData,newData):
        self.PreProcess(self,globalData,actualData,newData)
        input = {}
        output = {}
        for key,value in self.__FuzzySystem.variables.items():
            if isinstance(value, OutputVariable):
                output[key] = None
            if isinstance(value, InputVariable):
                ret,val = FuzzyBehavior.SearchVariable(key,globalData,actualData,newData)
                if ret:
                    input[key] =val
        self.__FuzzySystem.calculate(input,output)
        for i in output.items():
            key,value = i
            if key in self.OutputVars: self.OutputVars[key] = value
            for key in output:
                if key in actualData:
                    actualData[key]=output[key]
        self.UserDefinedProcess(self,globalData,actualData,newData)

    def __setattr__(self, key, value):
        if key == 'Process':
            object.__setattr__(self,'__UserDefinedProcess', value)
        else:
            super().__setattr__(key,value)

    @staticmethod
    def SearchVariable(key,globalData,actualData,newData):
        if key in actualData:
            return (True,actualData[key])
        if key in newData:
            return (True , newData[key])
        if key in globalData:
            return (True,globalData[key])
        return (False , 0)

    def Route(self,node):
        happiness_value = self.OutputVars['Happiness']
        if happiness_value is None:
            happiness_value = 0
            print('No se computo el sistema fuzzy')
        n=0
        for i in node.Successors():
            n = n +1
        n = n*happiness_value/10
        c=0
        for i in node.Successors():
            if c != n:
                c +=1
                yield i

    @staticmethod
    def Process_Opt():
        def ProcessOpt(self,globalData,actualData,newData):
            values = self.OutputVars
            for key in actualData:
                if not key in values and key in newData:
                    actualData[key] = newData[key]
        return ProcessOpt

    def Transform(self,key,value):
        if key == 'Love':
            val_send_to_love = self.OutputVars['LoveToSend']
            if val_send_to_love is None:
                pass
            return val_send_to_love
        else: return value