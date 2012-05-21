# -*- coding: utf8 -*-
import math

__author__ = 'Alejandro Piad'

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
