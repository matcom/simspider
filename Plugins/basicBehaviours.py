# -*- coding: utf8 -*-

from PropertyViewer import PropertyViewer
from manager import Plugin

Process = "Process"
Learn = "Learn"
Route = "Route"
Select = "Select"
Transform = "Transform"
Cleanup = "Cleanup"
OnSignal = "OnSignal"

class _BehaviourPluging(Plugin):
    def __init__(self, name, category, **kwargs):
        Plugin.__init__(self, "Behaviour.{0}".format(category))
        self.name = name
        self.kwargs = kwargs
        self.values = {}

    def setup(self):
        dlg = PropertyViewer(self.name, **self.kwargs)
        dlg.setValues(**self.values)

        if not self.kwargs or dlg.exec_():
            self.values = dlg.values()
            return self.getBehaviour()

    def getBehaviour(self):
        pass

class _ProcessBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Process, **kwargs)

class _LearnBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Learn, **kwargs)

class _RouteBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Route, **kwargs)

class _SelectBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Select, **kwargs)

class _TransformBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Transform, **kwargs)

class _CleanupBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, Cleanup, **kwargs)

class _OnSignalBehaviourPlugin(_BehaviourPluging):
    def __init__(self, name, **kwargs):
        _BehaviourPluging.__init__(self, name, OnSignal, **kwargs)

# Aqui están los behaviours definidos por nosotros
# David, esta es tu misión






