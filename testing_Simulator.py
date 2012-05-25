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
from behavior import Behavior
from simulator import Simulator
from node import Node

b = Behavior()
b.sendAfterReceive = True
b.includeBehavior = True
b.Process = be.BasicProcessing.UpdateAll()
b.Route = be.BasicRouting.All()
b.Select = be.BasicSelection.AllAtOnce(lambda:rdm.expovariate(1))
b.OnSignal = be.BasicSignaling.SendPeriodically(lambda:20)
b.Name = "first"

b1 = be.Behavior()
b1.Learn = be.BasicLearning.LearnAll()
b1.Name = "rest"

G=nx.DiGraph()
G.add_path([0,1,2,3,4])
for n in [Node(G,node) for node in G.nodes_iter()]:
    n["info"] = n.node
    if n.node==0:
        n.SetBehavior(b)
    else:
        n.SetBehavior(b1.Clone())

G.graph["temperature"] = 25
G.graph["presure"] = 45
G.graph["rain"] = 89

s = Simulator()
s.afterEvent.append(lambda x,y:input())

def aux(data):
    data["temperature"]+=1
    print("Globals processed")
s.SetInitialEvents([ ev.SignalAllNodes(G,None,0), ev.PeriodicalGraphEvent(0,G,lambda:rdm.expovariate(0.5),aux)])

s.Simulate()

print(s.timeSpent)
s.Simulate(time= 3)






