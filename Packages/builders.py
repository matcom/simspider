from PyQt4.QtCore import *

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

        for x,y in nodes:
            node = graph.addNode(QPoint(x + xpos, y + ypos))
            nodesIndex[index] = node
            index += 1
            node.setSelected(True)

        print(nodesIndex)

        for x,y in edges:
            graph.addEdge(nodesIndex[x], nodesIndex[y])

    def _createGraph(self):
        return [], []


