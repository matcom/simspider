# -*- coding: utf8 -*-

__author__ = 'Alejandro Piad'

from manager import Plugin
from builders import GraphBuilder
from PropertyViewer import *
import layout


class _BasicGraphBuilder(GraphBuilder, Plugin):
    def __init__(self, name, group, description, icon):
        GraphBuilder.__init__(self, name, group, description, icon)
        Plugin.__init__(self, "GraphBuilder")


class GridBuilder(_BasicGraphBuilder):
    def __init__(self):
        super().__init__("Grid", "Basic", "Inserts a unconected grid", "Resources/Grid.png")

    def _createGraph(self):
        dlg = PropertyViewer("Grid", "Resources/Grid.png",
            Columns=Integer(5,1,10),
            Rows=Integer(5,1,10),
            RowSpacing=Integer(50,50, 1000, 10),
            ColumnSpacing=Integer(50,50, 1000, 10))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            rows = values['Rows']
            columns = values['Columns']
            rspace = values['RowSpacing']
            cspace = values['ColumnSpacing']

            nodes = layout.grid2d(rows, columns, cspace, rspace)

        return nodes, edges


class CycleBuilder(_BasicGraphBuilder):
    def __init__(self):
        super().__init__("Cycle", "Basic", "Inserts directed cycle", "Resources/Cycle.png")

    def _createGraph(self):
        dlg = PropertyViewer("Cycle", "Resources/Cycle.png",
            Nodes=Integer(5,1,100))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']

            nodes = layout.circularNodes(n, 25)

            for x in range(n-1):
                edges.append((x,x+1))

            edges.append((n-1,0))

        return nodes, edges


class PathBuilder(_BasicGraphBuilder):
    def __init__(self):
        super().__init__("Path", "Basic", "Inserts a directed path", "Resources/Path.png")

    def _createGraph(self):
        dlg = PropertyViewer("Path", "Resources/Path.png",
            Nodes=Integer(5,1,100),
            Distance=Integer(60,60,1000,10))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']
            d = values['Distance']

            for i in range(n):
                nodes.append((i * d, 0))

            for x in range(n-1):
                edges.append((x,x+1))

        return nodes, edges


class CliqueBuilder(_BasicGraphBuilder):
    def __init__(self):
        super().__init__("Clique", "Basic", "Inserts a complete graph", "Resources/Clique.png")

    def _createGraph(self):
        dlg = PropertyViewer("Clique", "Resources/Clique.png",
            Nodes=Integer(5,1,100))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']

            nodes = layout.circularNodes(n, 25)

            for x in range(n):
                for y in range(n):
                    if x != y:
                        edges.append((x,y))

        return nodes, edges


class BipartiteBuilder(_BasicGraphBuilder):
    def __init__(self):
        super().__init__("Bipartite Graph", "Basic", "Inserts a bipartite graph", "Resources/Bipartite.png")

    def _createGraph(self):
        dlg = PropertyViewer("Bipartite", "Resources/Bipartite.png",
            LeftNodes=Integer(5,1,100),
            RightNodes=Integer(5,1,100),
            VerticalSpacing=Integer(50,50,1000, 10),
            HorizontalSpacing=Integer(100,100,1000, 10))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            l = values['LeftNodes']
            r = values['RightNodes']
            vs = values['VerticalSpacing']
            hs = values['HorizontalSpacing']

            y = -vs * l / 2

            for i in range(l):
                nodes.append((0, y))
                y += vs

            x = hs
            y = -r * vs / 2

            for i in range(r):
                nodes.append((x,y))
                y += vs

            for x in range(l):
                for y in range(r):
                    edges.append((x, y + l))

        return nodes, edges
