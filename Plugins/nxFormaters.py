# -*- coding: utf8 -*-
from PropertyViewer import PropertyViewer
from format import GraphReader, GraphWriter
from manager import Plugin

__author__ = 'Alejandro Piad'


class _NxReaderPlugin(GraphReader, Plugin):
    def __init__(self, name, extension, **kwargs):
        GraphWriter.__init__(self, name, extension)
        Plugin.__init__(self, "GraphFormater")

        self.kwargs = kwargs

    def read(self, path):
        dlg = PropertyViewer(**self.kwargs)

        if not self.kwargs or dlg.exec_:
            return self._readGraph(dlg.values())

        return None

    def _readGraph(self, values):
        pass


class _NxWriterPlugin(GraphWriter, Plugin):
    def __init__(self, name, extension, **kwargs):
        GraphWriter.__init__(self, name, extension)
        Plugin.__init__(self, "GraphFormater")

        self.kwargs = kwargs

    def write(self, path):
        dlg = PropertyViewer(**self.kwargs)

        if not self.kwargs or dlg.exec_:
            self._writeGraph(dlg.values())

        return None

    def _writeGraph(self, values):
        pass


