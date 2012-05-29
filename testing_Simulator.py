__author__ = 'David'
import sys
import os

gui_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Gui'))
packages_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Packages'))
redist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Redist'))
plugins_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Plugins'))
simulation_dir = os.path.join(packages_dir, 'Simulation')

sys.path.append(gui_dir)
sys.path.append(packages_dir)
sys.path.append(redist_dir)
sys.path.append(plugins_dir)
sys.path.append(simulation_dir)

print("Gui: {0}".format(gui_dir))
print("Packages: {0}".format(packages_dir))
print("Redist: {0}".format(redist_dir))
print("Plugins: {0}".format(plugins_dir))
print("Simulations: {0}".format(simulation_dir))

import networkx as nx
import behavior as be
import events as ev
import random as rdm
import gathering as ga
from behavior import Behavior
from simulator import Simulator
from node import Node
from node import NodePrototype


G=nx.DiGraph()
G.add_path([0,1,2,3,4])

b = Behavior()
#b.sendAfterReceive = True
#b.includeBehavior = True
#b.Process = be.BasicProcessing.UpdateAll()
b.Route = be.BasicRouting.All()
b.Select = be.BasicSelection.AllAtOnce(lambda:5)
b.OnSignal = be.BasicSignaling.SendPeriodically(lambda:20)
b.name = "first"

p1 = NodePrototype()
p1["health"] = 23
p1["money"] = 34
p1.DefineAttribute("love",45)
p1.SetBehavior(b)

p2 = NodePrototype()
p2.GetBehavior().sendAfterReceive = True
p2.GetBehavior().Select = be.BasicSelection.AllAtOnce(lambda:1)
p2.GetBehavior().Route = be.BasicRouting.All()
p2.GetBehavior().Process = be.BasicProcessing.UpdateAll()


p1.ApplyTo([0],G)
p2.ApplyTo([1,2,3,4],G)

#la simulacion ahora tambien puede manejar datos globales del grafo (serian los atributos del grafo)
G.graph["temperature"] = 25
G.graph["presure"] = 45
G.graph["rain"] = 89

#estos son los trackers que recopilan info (en este caso imprimen por consola lo que sucede)
ga.RegisterTracker(ga.NodeLog())

ga.RegisterTracker(ga.EdgeLog())
at = ga.AttributeTracker(["health"])
ga.RegisterTracker(at)

s = Simulator()
s.afterEvent.append(lambda x,y:input())
s.afterEvent.append(lambda x,y:print(at.attributesPath))

#ahora hay eventos a nivel de grafo (y asi poder, por ejemplo, actualizar la variables globales)
#ev.PeriodicalGraphEvent ejecuta periodicamte el metodo que se defina en este caso seria:
def aux(data):
    data["temperature"]+=1
    print("Globals processed")

#se definen los dos eventos iniciales
s.SetInitialEvents( [
                      ev.SignalAllNodes(G,None,0) ,
                      ev.PeriodicalGraphEvent(0,G,lambda:rdm.expovariate(0.5),aux)
                    ])
s.Simulate()
