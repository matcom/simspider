# -*- coding: utf8 -*-

#--------------------------------------------------------------------
# Agenda Distribuida
#--------------------------------------------------------------------
# Archivo : debug.py
#
# Resumen: Contiene las funcionalidades de debugging.
#
#--------------------------------------------------------------------


# IMPORTS: ----------------------------------------------------------

import datetime

from threading import Lock
from threading import currentThread

import functools

# GLOBALES: ---------------------------------------------------------
import traceback

_listeners = []

ERROR = 1
WARNING = 2
LOG = 3
INFO = 4
DEBUG = 5


# CLASES: -----------------------------------------------------------

class TraceListener(object):
    def __init__(self):
        self._filters = [('all', True)]
        self._indent = {}
        self._last_thread = None
        self.lock = Lock()
        self.verbose = 5

    def indent(self,category = None, level = DEBUG):
        if not self._filter(category, level):
            return

        t = _thread()
        ind = self._indent.get(t, 0)
        self._indent[t] = ind + 1

    def unindent(self, category = None, level = DEBUG):
        if not self._filter(category, level):
            return

        t = _thread()
        ind = self._indent[t]
        self._indent[t] = ind - 1

    def indentation(self):
        return self._indent.get(_thread(), 0)

    def filter(self, category, allow=True):
        self._filters.append(('all.' + category, allow))

    def resetFilters(self):
        self._filters = []

    def printMsg(self, msg, args, level = DEBUG, category = None):
        if not __debug__:
            return

        if not self._filter(category, level):
            return

        if args and not isinstance(args, tuple):
            args = (args,)

        # Agregar al mensaje espacios al inicio para indentar
        ind = 4
        lines = msg.split('\n')
        sep = " ...                                     | "

        if len(lines) == 1:
            lines = " " * self.indentation() * ind + lines[0]
        else:
            lines = " " * self.indentation() * ind + lines[0] + "\n" +\
            "\n".join([sep + " " * self.indentation() * ind + l for l in lines[1:]])

        msg =  "{0:40} | ".format("(" + (category or 'global') + ")") + lines

        self.lock.acquire()

        last = self._last_thread
        curr = _thread()

        if not last or curr != last:
            self.output(" Thread [{0}] ".format(curr).center(41, '=') + "|" + "=" * 50)

        self.output(msg, args)

        self._last_thread = curr

        self.lock.release()

    def output(self, msg, args = ()):
        pass

    def _filter(self, category, level):
        if self.verbose < level:
            return False

        if not category:
            category = 'all'
        else:
            category = 'all.' + category

        allow = False

        # Ver si existe alguna regla para esta categoria
        for cat, filter in self._filters:
            if _match(category, cat):
                allow = filter

        return allow


class StdoutListener(TraceListener):
    def __init__(self):
        TraceListener.__init__(self)

    def output(self, msg, args = ()):
        print(msg.format(*args))


class FileListener(TraceListener):
    def __init__(self, filename, mode = "a"):
        TraceListener.__init__(self)
        self.fd = open(filename, mode)
        self.fd.write("*" * 100 + "\n")
        self.fd.write("[ Timestamp: {0} ]\n".format(datetime.datetime.now()))


    def output(self, msg, args = ()):
        self.fd.write(msg.format(*args))
        self.fd.write("\n")
        self.fd.flush()

    def close(self):
        self.fd.close()

    def __del__(self):
        self.close()


# FUNCIONES: --------------------------------------------------------
def _match(category, c):
    count1 = len(category.split('.'))
    count2 = len(c.split('.'))
    c = '.'.join(c.split('.')[0:min(count1, count2)])
    return len(category) >= len(c) and category.startswith(c)

def _thread():
    return currentThread().getName()

def indent(category = None, level = DEBUG):
    for l in _listeners:
        l.indent(category, level)

def unindent(category = None, level = DEBUG):
    for l in _listeners:
        l.unindent(category, level)

def addListener(listener):
    _listeners.append(listener)

def clearListeners():
    global _listeners
    _listeners = []

# Imprimir un mensaje de debug
#
# @param msg : Texto del mensaje a imprimir
# @param priority : Valor numérico de la prioridad del mensaje
# @param log_file : Handle del archivo de log
#
def _printMsg(msg, args = (), level = DEBUG, category = None):
    for l in _listeners:
        l.printMsg(msg, args, level, category)

def _toStr(msg):
#    if isinstance(msg, str):
#         return msg.decode('utf8')
#    elif isinstance(msg, unicode):
#        return msg.encode('utf8')
#    else:
#        return unicode(msg)

    return msg

def error(function, exception, category = None, throw = True):
    if hasattr(exception, 'stack_trace'):
        exc = exception.message + "\n" + "".join(traceback.format_tb(exception.stack_trace))
    else:
        exc = exception.message

    _printMsg("(!!) Error ** In function '{0}' :\n{1}", (function, exc),
              level = ERROR, category = category)

    if throw:
        raise exception

def warning(msg, args = (), category = None):
    _printMsg("(!) Warning ** " + _toStr(msg), args, level = WARNING, category = category)

def log(msg, args = (), category = None):
    _printMsg("Log ** " + _toStr(msg), args, level = LOG, category = category)

def info (msg, args = (), category = None):
    _printMsg("Info ** " + _toStr(msg), args, level = INFO, category = category)

def debug(msg, args = (), category = None):
    _printMsg("Debug ** " + _toStr(msg), args, level = DEBUG, category = category)

def printDate(level = DEBUG, category = None):
    _printMsg("(*) Timestamp: {0}", datetime.datetime.now(), level = level, category = category)

def filter(category, allow=True):
    for l in _listeners:
        l.filter(category, allow)

def resetFilters():
    for l in _listeners:
        l.resetFilters()

# DECORATORS: ----------------------------------------------------------------

def trace(category = None, level = DEBUG):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            cat = category

            if not hasattr(function, "__calls"):
                function.__calls = 1
            else:
                function.__calls += 1

            if function.__class__.__name__ == 'function':
                name = function.__name__
            else:
                name = function.im_class.__name__ + '.' + function.__name__

            if not cat:
                cat = function.__module__.lower() + "." + name.lower()

            if function.__name__.startswith('_'):
                cat += ".private"

            _printMsg(">> {0}({1}, {2})", (name, args, kwargs),
                     category = cat)

            indent(cat, level)

            if __debug__:
                result = function(*args, **kwargs)
            else:
                try:
                    result = function(*args, **kwargs)
                except Exception as e:
                    error(name, e, category = cat, throw = False)

            unindent(cat, level)

            _printMsg("<< {0} = {1} (calls: {2})", (name, result, function.__calls),
                     category = cat)

            return result
        return wrapper
    if category and not level and hasattr(category, "__call__"):
        return decorator(category)
    else:
        return decorator


# CLASES: --------------------------------------------------------------------

class DebugParser(object):
    def __init__(self, stream):
          self.stream = stream


# MAIN: ----------------------------------------------------------------------

if __debug__:
    defaultListener = StdoutListener()
    addListener(defaultListener)


if __name__ == '__main__':
    import cmd

    class DebugCmd(cmd.Cmd):
        def __init__(self):
            cmd.Cmd.__init__(self)
            self.prompt = ">>> "

        def do_exit(self, args):
            return True


    DebugCmd().cmdloop("*** Debug Console ***\n\nType 'help' to begin.")

# FIN DE ARCHIVO: ---------------------------------------------------
