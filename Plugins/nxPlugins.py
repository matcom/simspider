# -*- coding: utf8 -*-

from PropertyViewer import *
from builders import GraphBuilder
from manager import Plugin

__author__ = 'Alejandro Piad'

class _NxPluginGraphBuilder(GraphBuilder, Plugin):
    def __init__(self, name, group, description, icon, **kwargs):
        GraphBuilder.__init__(self, name, group, description, icon)
        Plugin.__init__(self, "GraphBuilder")
        self.kwargs = kwargs

    def _createGraph(self):
        dlg = PropertyViewer(self.name, self.icon, **self.kwargs)

        nodes = []
        edges = []

        if dlg.exec_():
            values = dlg.values()
            G, nodes = self._getGraph(values)

            for i in G.edges_iter():
                edges.append(i)

        return nodes, edges

    def _getGraph(self, values):
        return None, []
