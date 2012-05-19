# -*- coding: utf8 -*-

"""
Módulo de configuración.
"""
import os

class Config(object):
    def __init__(self, path):
        self._conf = {}
        self._path = path

        fp = open(path, "r")
        self.readFile(fp)
        fp.close()

    def readFile(self, fp):
        lines = fp.readlines()
        while lines:
            l = lines.pop(0)[:-1]
            if l.startswith("[") and l.endswith("]"):
                sect = self.section(l[1:-1])
                sect.readLines(lines)

    def parseOptions(self, options):
        for arg in options:
            try:
                arg = arg.split('=')
                opt = arg[0].split('.')
                sect = opt[0]
                key = opt[1]
                val = arg[1]
                self.section(sect).set(key, val)
                print("Setting config option {0}.{1} = {2}".format(sect,key,val))
            except:
                print("Could not parse argument '{0}'".format(arg))

    def write(self, fp):
        for section in self.sections():
            fp.write("[{0}]\n".format(section.name()))
            section.write(fp)

    def flush(self):
        fp = open(self._path, "w")
        self.write(fp)
        fp.close()

    def section(self, item):
        if not item in self._conf:
            self._conf[item] = ConfigSection(item)

        return self._conf[item]

    def __getattr__(self, item):
        return self.section(item)

    def sections(self):
        for section in self._conf.keys():
            yield self._conf[section]


class ConfigSection(object):
    def __init__(self, name):
        self.__dict__['_data'] = {}
        self.__dict__['_name'] = name

    def __getattr__(self, item):
        if not self.hasItem(item):
            raise Exception("Item not present in config file: {0}".format(item))

        return self._data[item]

    def readLines(self, lines):
        while lines:
            l = lines[0][:-1]
            if l.startswith("[") and l.endswith("]"):
                return
            lines.pop(0)
            if l.startswith("#"):
                continue
            l = l.split("=")
            if len(l) < 2:
                continue
            key = l[0].lstrip().rstrip()
            value = l[1].lstrip().rstrip()
            self.set(key, self._parse(value))

    def write(self, fp):
        for key in self.items():
            value = self._data[key]
            fp.write("{0} = {1}\n".format(key, value))

        fp.write("\n")

    def __setattr__(self, key, value):
        self.set(key, value)

    def _parse(self, item):
        try: return int(item)
        except:
            if item == 'True' or item == 'true':
                return True
            elif item == 'False' or item == 'false':
                return False
            return item

    def get(self, item, default=None):
        if self.hasItem(item):
            return self._data[item]
        else:
            return default

    def set(self, key, value):
        self._data[key] = value

    def hasItem(self, item):
        return item in self._data

    def items(self):
        for key in self._data.keys():
            yield key

    def name(self):
        return self._name


if not os.path.exists("config.ini"):
    open("config.ini", "w").close()

config = Config("config.ini")

# FIN DEL ARCHIVO: --------------------------------------------------
