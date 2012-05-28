# -*- coding: utf8 -*-

from layout import *
import layout
from manager import Plugin
from PropertyViewer import *

__author__ = 'Alejandro Piad'

class _LayoutPlugin(Layout, Plugin):
    def __init__(self, name, description, icon, **kwargs):
        Plugin.__init__(self, "Layout")

        self.name = name
        self.description = description
        self.icon = icon
        self.kwargs = kwargs

    def _performLayout(self, nodes, edges):
        dlg = PropertyViewer(self.name, self.icon, **self.kwargs)

        if not self.kwargs or dlg.exec_():
            values = dlg.values()
            return self._getLayout(nodes, edges, values)

        return None

    def _getLayout(self, nodes, edges, values):
        pass


class CircularLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Cicular", "Layouts nodes in a circle", "CustomGraph.png")

    def _getLayout(self, nodes, edges, values):
        scale = 15
        return layout.circularNodes(len(nodes), scale)


class HorizontalDistributeLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Horizontal", "Layouts nodes in a horizontal line", "CustomGraph.png")

    def _getLayout(self, nodes, edges, values):
        return layout.horizontalNodes(len(nodes), 50)


class VerticalDistributeLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Vertical", "Layouts nodes in a vertical line", "CustomGraph.png")

    def _getLayout(self, nodes, edges, values):
        return layout.verticalNodes(len(nodes), 50)


class Grid2DLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Grid 2D", "Layouts nodes in a grid", "CustomGraph.png")

    def _getLayout(self, nodes, edges, values):
        r = int(math.sqrt(len(nodes)))
        c = len(nodes) // r

        while r * c < len(nodes):
            r += 1

        vspace = 75
        hspace = 75

        return layout.grid2d(r, c, hspace, vspace)[0:len(nodes)]


