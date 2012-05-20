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
