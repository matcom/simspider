# -*- coding: utf8 -*-
import math
import itertools

__author__ = 'Alejandro Piad'

class Layout:
    def apply(self, nodes):
        if not nodes or len(nodes) == 0:
            return

        xmid = 0
        ymid = 0

        for n in nodes:
            xmid += n.x()
            ymid += n.y()

        xmid /= len(nodes)
        ymid /= len(nodes)

        nodesDict = { x:y for y,x in enumerate(nodes) }
        outEdges = itertools.chain(*tuple(n.outEdges for n in nodesDict.keys()))
        edgeList = [(nodesDict[e.source], nodesDict[e.dest]) for e in outEdges if e.dest in nodesDict]
        nodeList = nodesDict.values()

        pos = self._performLayout(nodeList, edgeList)

        if not pos:
            return

        for p, node in zip(pos, nodes):
            x,y = p
            node.newX = x + xmid
            node.newY = y + ymid

    def _performLayout(self, nodes, edges):
        pass


def circularNodes(n, scale=1):
    nodes = []

    distance = scale * n
    start = 0 if n % 2 == 0 else -math.pi / 2

    for i in range(n):
        angle = start + 2 * i * math.pi / n
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        nodes.append((x,y))

    return nodes


def circularTree(h, r, scale=1):
    nodes = []
    n = 1

    for i in range(h):
        distance = scale * n
        start = 0 if n % 2 == 0 else -math.pi / 2

        for i in range(n):
            angle = start + 2 * i * math.pi / n
            x = distance * math.cos(angle)
            y = distance * math.sin(angle)
            nodes.append((x,y))

        n *= r

    return nodes


def grid2d(rows, columns, hscale=1, vscale=1):
    nodes = []

    x = -columns * hscale / 2
    y = -rows * vscale / 2

    for i in range(rows):
        for j in range(columns):
            nodes.append((x,y))
            x += hscale
        x = -columns * hscale / 2
        y += vscale

    return nodes


def verticalNodes(n, scale=1):
    y = -scale * n / 2
    nodes = []

    for i in range(n):
        nodes.append((0,y))
        y += scale

    return nodes


def horizontalNodes(n, scale=1):
    x = -scale * n / 2
    nodes = []

    for i in range(n):
        nodes.append((x,0))
        x += scale

    return nodes
