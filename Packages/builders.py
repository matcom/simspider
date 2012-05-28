from PyQt4.QtCore import *
from AddGraph import AddGraph
from GraphicNode import Subgraph, GraphicNode

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

        if len(nodes) + GraphicNode.visibleNodes > GraphicNode.maxVisibleNodes:
            hide = True
        else:
            hide = False

        subgraph = Subgraph(self.name, graph)

        dlg = AddGraph(self.name, graph)
        dlg.ui.progressBar.setMaximum(len(nodes))
        dlg.show()

        dlg.ui.status.setText("Adding nodes...")
        for x,y in nodes:
            node = graph.addNode(QPoint(x + xpos, y + ypos), subgraph)

            if hide:
                node.setNodeVisible(False)

            nodesIndex[index] = node
            index += 1
            dlg.ui.progressBar.setValue(index)

        index = 0
        dlg.ui.status.setText("Adding edges...")
        dlg.ui.progressBar.setMaximum(len(edges))
        dlg.ui.progressBar.setValue(0)
        for x,y in edges:
            graph.addEdge(nodesIndex[x], nodesIndex[y])
            index += 1
            dlg.ui.progressBar.setValue(index)

        dlg.close()

        graph.deselectAll()

        for node in nodesIndex.values():
            node.setSelected(True)

    def _createGraph(self):
        return [], []


