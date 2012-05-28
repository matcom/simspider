# -*- coding: utf8 -*-
from PropertyViewer import Float

__author__ = 'Alejandro Piad'

from basicLayout import _LayoutPlugin
import networkx as nx

class _NxLayoutPlugin(_LayoutPlugin):
    def _getLayout(self, nodes, edges, values):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        layout = self._applyLayout(G, values)

        return [(float(layout[n][0]) * 250, float(layout[n][1]) * 250) for n in nodes]


    def _applyLayout(self, G, values):
        pass


try:
    import numpy

    class SpringLayout(_NxLayoutPlugin):
        def __init__(self):
            _NxLayoutPlugin.__init__(self, "Spring", "Layouts items with a spring-mass system", "CustomGraph.png")

        def _applyLayout(self, G, values):
            return nx.spring_layout(G)


    class RandomLayout(_NxLayoutPlugin):
        def __init__(self):
            _NxLayoutPlugin.__init__(self, "Random", "Layouts items randomly", "CustomGraph.png")

        def _applyLayout(self, G, values):
            return nx.random_layout(G)

except:
    pass

