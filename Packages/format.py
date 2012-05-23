# -*- coding: utf8 -*-

author__ = 'Alejandro Piad'

class GraphReader:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def read(self, path):
        pass


class GraphWriter:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def write(self, path):
        pass
