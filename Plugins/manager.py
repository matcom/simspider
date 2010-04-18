# -*- coding: utf8 -*-
import os
import debug

__author__ = 'Alejandro Piad'

class PluginManager:
    def __init__(self):
        self._categories = {}


    @debug.trace()
    def loadPlugins(self):
        for file in os.listdir("Plugins"):
            if not file in ["__init__.py", "manager.py"] and file.endswith(".py"):
                self.load(file[0:-3])


    @debug.trace()
    def load(self, file):
        debug.debug("Loading module {0}", (file,), "plugins")

        try:
            module = __import__(file)

            for name, type in module.__dict__.items():
                if type.__class__.__name__ == "type":
                    self.loadType(type, file)

        except Exception as e:
            debug.warning("Error loading module {0}. Error: {1}.", (file, e), "plugins")


    @debug.trace()
    def registerItem(self, category, item):
        list = []

        if category in self._categories:
            list = self._categories[category]
        else:
            self._categories[category] = list

        list.append(item)
        debug.info("Registered plugin {0} in {1}", (item.__class__.__name__, category), "plugins")


    @debug.trace()
    def getItems(self, category):
        return self._categories.get(category, [])


    @debug.trace()
    def loadType(self, type, module):
        if type.__name__.startswith("_"):
            return
        if not type.__module__ == module:
            return

        try:
            debug.debug("Attempting to load plugin type {0}", (type.__name__,), "plugins")

            item = type()
            item.load(self)

        except Exception as e:
            debug.warning("Couldn't load type {0}. Error: {1}.", (type.__name__, e), "plugins")


class Plugin:
    def __init__(self, category):
        self.category = category

    def load(self, manager):
        manager.registerItem(self.category, self)
