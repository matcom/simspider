# -*- coding: utf8 -*-

from PropertyViewer import *

from builders import GraphBuilder
from manager import Plugin

from nxPlugins import _NxPluginGraphBuilder

import networkx.generators.random_graphs as rnd
import layout

__author__ = 'Alejandro Piad'


class ErdosRenyiGraphBuilder(_NxPluginGraphBuilder):
    def __init__(self):
        super().__init__("Erdös-Rényi", "Random", "Inserts a random graph", "Resources/CustomGraph.png",
            Nodes=IntegerBuilder(5, 1, 100, 1),
            Density=FloatBuilder(0.5))

    def _getGraph(self, values):
        n = values['Nodes']
        p = values['Density']

        G = rnd.fast_gnp_random_graph(n, p, directed=True)
        nodes = layout.circularNodes(n, 25)

        return G, nodes


class NewmanWattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Newman-Watys-Strogatz", "Random", "Inserts a 'small world' network", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class WattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Watys-Strogatz", "Random", "Inserts a 'small world' network", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class ConnectedWattsStrogatzGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Watys-Strogatz (Connected)", "Random", "Inserts a 'small world' network", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class BarabasiAlbertGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Barabasi-Albert", "Random", "Inserts a random biassed graph", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomRegularGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Regular", "Random", "Inserts a random regular graph", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class PowerlawClusterGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Powerlaw Cluster", "Random", "Inserts a random powerlaw graph", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomLobsterGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Lobster", "Random", "Inserts a random lobster graph", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomShellGraphBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Random Shell", "Random", "Inserts a random shell graph", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges


class RandomPowerlawTreeBuilder(GraphBuilder, Plugin):
    def __init__(self):
        GraphBuilder.__init__(self, "Powerlaw Tree", "Random", "Inserts a random powerlaw tree", "Resources/CustomGraph.png")
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

            nodes = layout.circularNodes(n, 25)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges
