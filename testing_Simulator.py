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

b = Behavior()
b.sendAfterReceive = True
b.includeBehavior = True
b.Process = be.BasicProcessing.UpdateAll()
b.Route = be.BasicRouting.All()
b.Select = be.BasicSelection.OneByOne(lambda:rdm.expovariate(1))
b.OnSignal = be.BasicSignaling.SendPeriodically(lambda:20)
b.Name = "first"

b1 = be.Behavior()
b1.Learn = be.BasicLearning.LearnAll()
b1.Name = "rest"

G=nx.DiGraph()
G.add_path([0,1,2,3,4])
for n in [Node(G,node) for node in G.nodes_iter()]:
    #ya se pueden agregar atributos al nodo como si fuera un diccionario normal
    n["info"] = n.node
    n["info2"] = n.node+10
    #lista de atributos
    print(list(n.Attributes()) )
    #lista de atributos incluido el atributo que almacena el behavior
    print(list(n.Attributes(inclBehavior=True)) )
    if n.node==0:
        n.SetBehavior(b)
    else:
        #ya se pueden clonar los behaviors
        n.SetBehavior(b1.Clone())

#la simulacion ahora tambien puede manejar datos globales del grafo (serian los atributos del grafo)
G.graph["temperature"] = 25
G.graph["presure"] = 45
G.graph["rain"] = 89

#estos son los trackers que recopilan info (en este caso imprimen por consola lo que sucede)
ga.RegisterTracker(ga.NodeLog())
ga.RegisterTracker(ga.EdgeLog())

s = Simulator()
s.afterEvent.append(lambda x,y:input())

#ahora hay eventos a nivel de grafo (y asi poder actualizar la variables globales por ejemplo)
#ev.PeriodicalGraphEvent ejecuta periodicamte el metodo que se defina en este caso seria:
def aux(data):
    data["temperature"]+=1
    print("Globals processed")

#se definen los dos eventos iniciales
s.SetInitialEvents([ ev.SignalAllNodes(G,None,0), ev.PeriodicalGraphEvent(0,G,lambda:rdm.expovariate(0.5),aux)])
s.Simulate()







