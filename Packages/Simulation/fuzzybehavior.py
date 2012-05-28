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
    def __init__(self,path = None, system = None):
        super().__init__()
        object.__setattr__(self,'PreProcess',type(self).PreProcess)
        if path is None :
            self.__FuzzySystem = system
        else :
            self.__FuzzySystem = Redist.pyfuzzy.storage.fcl.Reader.Reader().load_from_file(path)
        self.OutputVars = {}
        for key,value in self.__FuzzySystem.variables.items():
            if isinstance(value,OutputVariable):
                self.OutputVars[key]=None
        def __EmptyProcess(self,globalData,actualData,newData): pass
        self.UserDefinedProcess = __EmptyProcess


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
            object.__setattr__(self,'UserDefinedProcess', value)
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