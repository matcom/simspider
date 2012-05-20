import math

from PyQt4.QtCore import *
from PropertyViewer import *
import tools

__author__ = 'Alejandro Piad'

class GraphBuilder:
    def __init__(self, name, description, icon):
        self.name = name
        self.description = description
        self.icon = icon

    def build(self, graph, xpos, ypos):
        nodes, edges = self._createGraph()
        nodesIndex = {}
        index = 0

        for x,y in nodes:
            node = graph.addNode(QPoint(x + xpos, y + ypos))
            nodesIndex[index] = node
            index += 1
            node.setSelected(True)

        for x,y in edges:
            graph.addEdge(nodesIndex[x], nodesIndex[y])

    def _createGraph(self):
        return [], []


class GridBuilder(GraphBuilder):
    def __init__(self):
        super().__init__(None, None, None)

    def _createGraph(self):
        dlg = PropertyViewer("Grid", "Resources/Grid.png",
            Columns=IntegerBuilder(5,1,10),
            Rows=IntegerBuilder(5,1,10),
            RowSpacing=IntegerBuilder(50,50, 1000, 10),
            ColumnSpacing=IntegerBuilder(50,50, 1000, 10))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            rows = values['Rows']
            columns = values['Columns']
            rspace = values['RowSpacing']
            cspace = values['ColumnSpacing']

            x = -columns * cspace / 2
            y = -rows * rspace / 2

            for i in range(rows):
                for j in range(columns):
                    nodes.append((x,y))
                    x += cspace
                x = 0
                y += rspace

        return nodes, edges


class CycleBuilder(GraphBuilder):
    def __init__(self):
        super().__init__(None, None, None)

    def _createGraph(self):
        dlg = PropertyViewer("Cycle", "Resources/Cycle.png",
            Nodes=IntegerBuilder(5,1,100))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']

            nodes = tools.circularNodes(n, 25)

            for x in range(n-1):
                edges.append((x,x+1))

            edges.append((n-1,0))

        return nodes, edges


class PathBuilder(GraphBuilder):
    def __init__(self):
        super().__init__(None, None, None)

    def _createGraph(self):
        dlg = PropertyViewer("Path", "Resources/Path.png",
            Nodes=IntegerBuilder(5,1,100),
            Distance=IntegerBuilder(60,60,1000,10))

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


class CliqueBuilder(GraphBuilder):
    def __init__(self):
        super().__init__(None, None, None)

    def _createGraph(self):
        dlg = PropertyViewer("Clique", "Resources/Clique.png",
            Nodes=IntegerBuilder(5,1,100))

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            n = values['Nodes']

            nodes = tools.circularNodes(n, 25)

            for x in range(n):
                for y in range(n):
                    if x != y:
                        edges.append((x,y))

        return nodes, edges


class BipartiteBuilder(GraphBuilder):
    def __init__(self):
        super().__init__(None, None, None)

    def _createGraph(self):
        dlg = PropertyViewer("Bipartite", "Resources/Bipartite.png",
            LeftNodes=IntegerBuilder(5,1,100),
            RightNodes=IntegerBuilder(5,1,100),
            VerticalSpacing=IntegerBuilder(50,50,1000, 10),
            HorizontalSpacing=IntegerBuilder(100,100,1000, 10))

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
