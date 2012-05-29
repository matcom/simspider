# -*- coding: utf8 -*-
from Code import CodeDialog

from PropertyViewer import *
from manager import Plugin

Process = "Process"
Learn = "Learn"
Route = "Route"
Select = "Select"
Transform = "Transform"
Cleanup = "Cleanup"
OnSignal = "OnSignal"

from Simulation import behavior

class _BehaviourPluging(Plugin):
    def __init__(self, name, category, **kwargs):
        Plugin.__init__(self, "Behaviour.{0}".format(category))
        self.name = name
        self.kwargs = kwargs
        self.values = {}

    def setup(self):
        dlg = PropertyViewer(self.name, **self.kwargs)
        # dlg.setValues(**self.values)

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

# Custom behaviours

class _CustomBehaviour(_BehaviourPluging):
    def __init__(self, name, category, function, args=(), **kwargs):
        _BehaviourPluging.__init__(self, name, category, **kwargs)
        self.function = function
        self.args = args

    def getBehaviour(self):
        dlg = CodeDialog(self.function, self.args)

        if dlg.exec_():
            return dlg.compile()

        return None

class CustomProcessBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Process, "Process", ("self", "globalData", "actualData", "newData"))

class CustomLearnBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Learn, "Learn", ("self", "new"))

class CustomRouteBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Route, "Route", ("self", "node"))

class CustomSelectBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Select, "Select", ("self", "destination", "data", "actTime"))

class CustomTransformBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Transform, "Transform", ("self", "key", "value"))

class CustomCleanupBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", Cleanup, "Cleanup", ("self", "data"))

class CustomOnSignalBehaviour(_CustomBehaviour):
    def __init__(self):
        _CustomBehaviour.__init__(self, "Custom", OnSignal, "OnSignal", ("self", "node", "signalData", "actualTime"))

# Fin de los behaviours custom

# Behaviours por defecto

class UpdateAllBehaviour(_ProcessBehaviourPlugin):
    def __init__(self):
        _ProcessBehaviourPlugin.__init__(self, "Update All")

    def getBehaviour(self):
        return behavior.BasicProcessing.UpdateAll()


class UpdateBehaviour(_ProcessBehaviourPlugin):
    def __init__(self):
        _ProcessBehaviourPlugin.__init__(self,"Update Specific Keys",
                                         Keys=String())

    def getBehaviour(self):
        return behavior.BasicProcessing.Update(self.values['Keys'].split())


class LearnAllBehaviour(_LearnBehaviourPlugin):
    def __init__(self):
        _LearnBehaviourPlugin.__init__(self, "Learn All")

    def getBehaviour(self):
        return behavior.BasicLearning.LearnAll()


class LearnSpecificBehaviour(_LearnBehaviourPlugin):
    def __init__(self):
        _LearnBehaviourPlugin.__init__(self, "Learn Specific Behaviour",
                                       SendAfterReceive=Bool(),
                                       IncludeBehaviour=Bool(),
                                       Process=Bool(),
                                       Learn=Bool(),
                                       Route=Bool(),
                                       Select=Bool(),
                                       Transform=Bool(),
                                       Cleanup=Bool(),
                                       Signaling=Bool(),
                                       )

    def getBehaviour(self):
        return behavior.BasicLearning.LearnSpecificBehavior(
            sendAftReceive=self.values['SendAfterReceive'],
            sendBeh=self.values['IncludeBehaviour'],
            process=self.values['Process'],
            learn=self.values['Learn'],
            route=self.values['Route'],
            select=self.values['Select'],
            transform=self.values['Transform'],
            signaling=self.values['Signaling'],
        )


class RouteAllBehaviour(_RouteBehaviourPlugin):
    def __init__(self):
        _RouteBehaviourPlugin.__init__(self, "Route All")

    def getBehaviour(self):
        return behavior.BasicRouting.All()


class RouteSampleBehaviour(_RouteBehaviourPlugin):
    def __init__(self):
        _RouteBehaviourPlugin.__init__(self, "Route Sample", Count=Integer(1,0,1000000))

    def getBehaviour(self):
        return behavior.BasicRouting.Sample(self.values['Count'])


class SelectAllAtOnceBehaviour(_SelectBehaviourPlugin):
    def __init__(self):
        import random
        _SelectBehaviourPlugin.__init__(self, "All At Once",
                                        TimeFunction=Code("timeFunction", (), { "random": random }))

    def getBehaviour(self):
        return behavior.BasicSelection.AllAtOnce(self.values['TimeFunction'])


class SelectOneByOneBehaviour(_SelectBehaviourPlugin):
    def __init__(self):
        import random
        _SelectBehaviourPlugin.__init__(self, "One By One",
                                        TimeFunction=Code("timeFunction", (), { "random": random }))

    def getBehaviour(self):
        return behavior.BasicSelection.OneByOne(self.values['TimeFunction'])


class SelectSpecificGroupBehaviour(_SelectBehaviourPlugin):
    def __init__(self):
        import random
        _SelectBehaviourPlugin.__init__(self, "Specific Group",
                                        Keys=String(),
                                        TimeFunction=Code("timeFunction", (), { "random": random }))

    def getBehaviour(self):
        return behavior.BasicSelection.SpecificGroup(self.values['Keys'].split(), self.values['TimeFunction'])


class SendOnSignalBehaviour(_OnSignalBehaviourPlugin):
    def __init__(self):
        super().__init__("Send On Signal")

    def getBehaviour(self):
        return behavior.BasicSignaling.SendOnSignal()


class SendPeriodicallyBehaviour(_OnSignalBehaviourPlugin):
    def __init__(self):
        import random
        super().__init__("Send Periodically", TimeFunction=Code("timeFunction", (), { "random": random }))

    def getBehaviour(self):
        return behavior.BasicSignaling.SendPeriodically(self.values['TimeFunction'])
