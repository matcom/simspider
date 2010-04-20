from PyQt4.QtCore import *
from GraphicNode import Subgraph

__author__ = 'Alejandro Piad'

class GraphBuilder:
    def __init__(self, name, group, description, icon):
        self.name = name
        self.description = description
        self.icon = icon
        self.group = group

    def build(self, graph, xpos, ypos):
        nodes, edges = self._createGraph()
        nodesIndex = {}
        index = 0

        subgraph = Subgraph(self.name, graph)

        for x,y in nodes:
            node = graph.addNode(QPoint(x + xpos, y + ypos), subgraph)
            nodesIndex[index] = node
            index += 1

        for x,y in edges:
            graph.addEdge(nodesIndex[x], nodesIndex[y])

        graph.deselectAll()

        for node in nodesIndex.values():
            node.setSelected(True)

    def _createGraph(self):
        return [], []


