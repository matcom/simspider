# -*- coding: utf8 -*-

__author__ = 'David'

import networkx as nx
import behavior as beh
import events as ev
import random as rdm
from simulator import Simulator
from node import Node

b = beh.Behavior()
b.sendAfterReceive = False
b.includeBehavior = True
b.Process = beh.BasicProcessing.UpdateAll()
b.Rout = beh.BasicRouting.All()
b.Select = beh.BasicSelection.AllAtOnce(lambda:rdm.expovariate(1))
b.OnSignal = beh.BasicSignaling.SendPeriodically(lambda:20)
b.Name = "first"

G=nx.DiGraph()
G.add_cycle([0,1,2,3,4])
for n in [Node(G,node) for node in G.nodes_iter()]:
    n.SetAttribute("info",n.node)
    if n.node==0:
        n.SetBehavior(b)
    else:
        b1 = beh.Behavior()
        b1.Learn = beh.BasicLearning.LearnAll()
        b1.Name = "rest"
        n.SetBehavior(b1)

s = Simulator()
s.after_event.append(lambda x,y:input())
s.InsertEvents([ev.SignalAllNodes(G,None,0)])
s.Simulate()

print(s.time_spent)
s.Simulate(time= 3)






