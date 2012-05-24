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
        _LayoutPlugin.__init__(self, "Cicular", "Layouts nodes in a circle", "CustomGraph.png",
            Scale=FloatBuilder(25.0,0.0,100.0,5.0))

    def _getLayout(self, nodes, edges, values):
        scale = values['Scale']
        return layout.circularNodes(len(nodes), scale)


class HorizontalDistributeLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Horizontal", "Layouts nodes in a horizontal line", "CustomGraph.png",
            Scale=FloatBuilder(50.0,0.0,100.0,5.0))

    def _getLayout(self, nodes, edges, values):
        return layout.horizontalNodes(len(nodes), values['Scale'])


class VerticalDistributeLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Vertical", "Layouts nodes in a vertical line", "CustomGraph.png",
            Scale=FloatBuilder(50.0,0.0,100.0,5.0))

    def _getLayout(self, nodes, edges, values):
        return layout.verticalNodes(len(nodes), values['Scale'])


class Grid2DLayout(_LayoutPlugin):
    def __init__(self):
        _LayoutPlugin.__init__(self, "Grid 2D", "Layouts nodes in a grid", "CustomGraph.png",
            Rows=IntegerBuilder(5,1,100,1),
            VerticalSpace=FloatBuilder(50.0,0.0,100.0,1.0),
            HorizontalSpace=FloatBuilder(50.0,0.0,100.0,1.0))

    def _getLayout(self, nodes, edges, values):
        r = values['Rows']
        c = len(nodes) // r
        vspace = values['VerticalSpace']
        hspace = values['HorizontalSpace']

        return layout.grid2d(r, c, hspace, vspace)[0:len(nodes)]


