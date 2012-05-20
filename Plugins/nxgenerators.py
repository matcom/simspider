# -*- coding: utf8 -*-

from PropertyViewer import *

from builders import GraphBuilder
from manager import Plugin

import networkx.generators.random_graphs as rnd
import tools

__author__ = 'Alejandro Piad'

class ErdosRenyiGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Erdös-Rényi", "Inserts a random uniform graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Density=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            p = values['Density']

            G = rnd.fast_gnp_random_graph(n, p, directed=True)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class NewmanWattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Newman-Watys-Strogatz", "Inserts a 'small world' network", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Neighboors=IntegerBuilder(2,1,100,1),
            Density=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            k = values['Neighboors']
            p = values['Density']

            G = rnd.newman_watts_strogatz_graph(n, k, p)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class WattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Watys-Strogatz", "Inserts a 'small world' network", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Neighboors=IntegerBuilder(2,1,100,1),
            Density=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            k = values['Neighboors']
            p = values['Density']

            G = rnd.watts_strogatz_graph(n, k, p)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class ConnectedWattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Watys-Strogatz (Connected)", "Inserts a 'small world' network", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Neighboors=IntegerBuilder(2,1,100,1),
            Density=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            k = values['Neighboors']
            p = values['Density']

            G = rnd.connected_watts_strogatz_graph(n, k, p)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class BarabasiAlbertGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Barabasi-Albert", "Inserts a random biassed graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Degree=IntegerBuilder(2,1,100,1))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            m = values['Degree']

            G = rnd.barabasi_albert_graph(n, m)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomRegularGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Regular", "Inserts a random regular graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Degree=IntegerBuilder(2,1,100,1))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            m = values['Degree']

            G = rnd.random_regular_graph(m, n)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class PowerlawClusterGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Powerlaw Cluster", "Inserts a random powerlaw graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Degree=IntegerBuilder(2,1,100,1),
            TriangleDensity=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            m = values['Degree']
            p = values['TriangleDensity']

            G = rnd.powerlaw_cluster_graph(m, n, p)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomLobsterGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Lobster", "Inserts a random lobster graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            ExpectedNodes=IntegerBuilder(5, 1, 100, 1),
            BackboneDensity=FloatBuilder(0.5),
            Density=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['ExpectedNodes']
            p1 = values['BackboneDensity']
            p2 = values['Density']

            G = rnd.random_lobster(n, p1, p2)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomShellGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Shell", "Inserts a random shell graph", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Edges=IntegerBuilder(10, 1, 100, 1),
            Ratio=FloatBuilder(0.5))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            m = values['Edges']
            d = values['Ratio']

            G = rnd.random_shell_graph([(n,m,d)])

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomPowerlawTreeBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Powerlaw Tree", "Inserts a random powerlaw tree", "Resources/CustomGraph.png")
        Plugin.__init__(self, "GraphBuilder")

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon,
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Gamma=FloatBuilder(3,0,10,0.1))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            g = values['Gamma']

            G = rnd.random_powerlaw_tree(n, g)

            nodes = tools.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges
