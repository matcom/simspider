# -*- coding: utf8 -*-
from PropertyViewer import IntegerBuilder
import layout

__author__ = 'Alejandro Piad'

from nxPlugins import _NxPluginGraphBuilder
import networkx as nx

class BalancedTreeGraphBuilder(_NxPluginGraphBuilder):
    def __init__(self):
        super().__init__("Balanced Tree", "Standard", "Inserts a perfectly balanced tree", "Resources/CustomGraph.png",
        Branching=IntegerBuilder(2,1,10,1),
        Height=IntegerBuilder(5,1,100,1))

    def _getGraph(self, values):
        r = values['Branching']
        h = values['Height']

        G = nx.balanced_tree(r ,h, create_using=nx.DiGraph())
        nodes = layout.circularTree(h, r, 25)

        return G, nodes


class CircularLadderGraphBuilder(_NxPluginGraphBuilder):
    def __init__(self):
        super().__init__("Circular Ladder", "Standard", "Inserts two linked concentric rings", "Resources/CustomGraph.png",
            Nodes=IntegerBuilder(5,1,100,1))

    def _getGraph(self, values):
        n = values['Nodes']

        G = nx.circular_ladder_graph(n)
        nodes = layout.circularNodes(n, 20) + layout.circularNodes(n, 40)

        return G, nodes


class ConnectedGridGraphBuilder(_NxPluginGraphBuilder):
    def __init__(self):
        super().__init__("Connected Grid 2D", "Standard", "Inserts an N x M connected grid", "Resources/CustomGraph.png",
            Rows=IntegerBuilder(5,1,100,1),
            Columns=IntegerBuilder(5,1,100,1))

    def _getGraph(self, values):
        n = values['Rows']
        m = values['Columns']

        G = nx.grid_2d_graph(m, n)
        edges = []

        for i,j in G.edges_iter():
            xi, yi = i
            xj, yj = j
            edges.append((xi * m + yi, xj * m + yj))

        G.edges_iter = lambda: edges

        nodes = layout.grid2d(n ,m, 50, 50)

        return G, nodes
