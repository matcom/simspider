# -*- coding: utf8 -*-
from PropertyViewer import FloatBuilder

__author__ = 'Alejandro Piad'

from basicLayout import _LayoutPlugin
import networkx as nx

class _NxLayoutPlugin(_LayoutPlugin):
    def _getLayout(self, nodes, edges, values):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        return self._applyLayout(G, values)

    def _applyLayout(self, G, values):
        pass


try:
    import numpy

    class SpringLayout(_NxLayoutPlugin):
        def __init__(self):
            _NxLayoutPlugin.__init__(self, "Spring", "Layouts item with a spring-mass system", "CustomGraph.png")

        def _applyLayout(self, G, values):
            return nx.spring_layout(G)


    class RandomLayout(_NxLayoutPlugin):
        def __init__(self):
            _NxLayoutPlugin.__init__(self, "Spring", "Layouts item with a spring-mass system", "CustomGraph.png",
                Scale=FloatBuilder(25.0,0.0,100.0,1.0))

        def _applyLayout(self, G, values):
            scale = values['Scale']
            return ((x * scale, y * scale) for x,y in nx.random_layout(G))

except:
    pass

