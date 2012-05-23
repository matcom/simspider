# -*- coding: utf8 -*-

"""
Define funcionalidades relacionadas con el multi-threading.

"""

import functools

__all__ = ['Async',
           'async',
           'synchronized',
           'instance_wide_sync',
           'instance_sync',
           'instance_shared_sync',
           'static_sync']

from threading import Thread, Lock
import debug

# Importando excepciones de Pyro
from exceptions import *

from eventhandles import Event

class _Timeout(object):
    def __nonzero__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, _Timeout)


TIMEOUT = _Timeout()


class Async(Thread):
    """
    Envuelve una funcion (callable) para ser ejecutada en un hilo independiente.
    """

    done = Event('done', True)
    fail = Event('fail', True)
    result = Event('result', True)

    def __init__(self, callable, args = (), kwargs = None):
        debug._printMsg("Building AsyncBase {0}".format(callable))
        Thread.__init__(self)
        self.setDaemon(True)
        self.setName("Async '{0}'".format(callable.__name__))
        self.callable = callable
        self.args = args
        self.kwargs = kwargs or {}
        self.lock = Lock()
        self._finish = False
        self._exception = None

    @debug.trace()
    def run(self):
        try:
            debug._printMsg("Runnning thread {0}".format(self.name))
            self.runSync()
            self.done()
            self.result(self._value)

        except Exception as e:
            trace = sys.exc_traceback
            self._exception = e
            self._exception.stack_trace = trace
            debug.error(self.run, self._exception, throw = False)

            self.fail(self._exception)

        self._finish = True

    @debug.trace()
    def runSync(self):
        debug._printMsg("Executing bound method {0}".format(self.callable))
        self._value = self.callable(*self.args, **self.kwargs)

    @debug.trace()
    def join(self, timeout=None):
        Thread.join(self, timeout)

        if self._exception:
            debug.error(self.join, self._exception, throw = True)

        return self._finish or TIMEOUT

    @debug.trace()
    def value(self, timeout = None, default = TIMEOUT):
        if not self.join(timeout):
            return default

        return self._value if hasattr(self, "_value") else default


def async(callable):
    @functools.wraps(callable)
    def wrapper(*args, **kwargs):
        async = Async(callable, args, kwargs)
        async.start()
        return async
    return wrapper


def safeAsync(callable):
    @functools.wraps(callable)
    def wrapper(*args, **kwargs):
        @async
        def asyncCycle(*args, **kwargs):
            while True:
                try:
                    async = Async(callable, args, kwargs)
                    async.start()
                    return async.value()
                except:
                    continue
        return asyncCycle(*args, **kwargs)
    return wrapper


def synchronized(lock = None, instance = False, category = None):
    """
    Envuelve un callable en un región crítica para hacerlo thread-safe.

    Para funciones globales, todos los argumentos por defecto están bien.
    Si se quiere sincronizar más de una función a la vez, se puede
    pasar un objecto lock-like (param lock) que se usará para bloquear.

    Para métodos de instancia, especificar instance = True. En este caso
    la función se bloqueará para cada instancia. attribute puede ser
    definido a un nombre de un campo donde se almacenará un Lock() para
    bloquear esta instancia. Si no especifica, se crea un por defecto
    de nombre __<callable>_lock. Esto garantiza que cada método de cada
    instancia se sincroniza de manera independiente.
    Se puede especificar un nombre
    para permitir que diferentes métodos se sincronicen juntos.

    NOTE 1: Si lock is not None entonces se obvian el resto de los argumentos,
    aun cuando instance = True.

    NOTE 2: Si instance = True se asume que el primer argumento del callable
    es self.
    """
    def decorator(callable):
        if lock:
            callable.__lock = lock
        elif not instance:
            callable.__lock = Lock()
        elif category:
            callable.__attribute = "__{0}_lock".format(category)
        else:
            callable.__attribute = "__{0}_lock".format(callable.__name__)

        @functools.wraps(callable)
        def static_wrapper(*args, **kwargs):
            lock = callable.__lock
            lock.acquire()
            # lock.current = currentThread()
            result = callable(*args, **kwargs)
            # lock.current = None
            lock.release()
            return result

        @functools.wraps(callable)
        def instance_wrapper(self, *args, **kwargs):
            if not hasattr(self, callable.__attribute):
                setattr(self, callable.__attribute, Lock())

            lock = getattr(self, callable.__attribute)
            lock.acquire()
            # lock.current = currentThread()
            result = callable(self, *args, **kwargs)
            # lock.current = None
            lock.release()
            return result

        if lock or not instance:
            return static_wrapper
        else:
            return instance_wrapper

    return decorator


def instance_wide_sync(callable):
    """
    Decora una funcion (callable) para ser sincronizada a nivel de instancia.

    Garantiza que todos los metodos de instancia decorados con esta funcion
    estan sincronizados entre si, es decir, ningun metodo puede ser accecido
    desde una hebra si otro metodo esta siendo accedido por una hebra
    distina.
    """
    return synchronized(None, True, '__lock')(callable)


def instance_sync(callable):
    """
    Decora una funcion (callable) para ser sincronizada.

    Garantiza que todos los llamados a esta funcion en una
    misma instancia están sincronizados entre sí.
    """
    return synchronized(None, True, None)(callable)


def instance_shared_sync(category):
    """
    Decora una funcion para ser sincronizada a nivel de instancia con otras.

    Garantiza que todas las funciones de la misma instancia decoradas con la
    misma categoria estan sincronizadas entre si con un mismo lock.
    """
    return synchronized(None, True, category)


def static_sync(callable):
    return synchronized()(callable)


class Sync(object):
    """
    Envuelve un objecto para que todos sus llamados sean ejectudos de manera thread-safe.
    """

    def __init__(self, item, lock = None):
        self.__dict__['_item'] = item
        self.__dict__['__item_lock'] = lock or Lock()

    @instance_shared_sync('item')
    def __call__(self, *args, **kwargs):
        return self._item(*args, **kwargs)

    @instance_shared_sync('item')
    def __getattr__(self, item):
        return getattr(self._item, item)

    @instance_shared_sync('item')
    def __setattr__(self, key, value):
        setattr(self._item, key, value)

    @instance_shared_sync('item')
    def __getitem__(self, item):
        return self._item.__getitem__(item)

    @instance_shared_sync('item')
    def __setitem__(self, key, value):
        self._item.__setitem__(key, value)

    @instance_shared_sync('item')
    def __contains__(self, item):
        return self._item.__contains__(item)

    @instance_shared_sync('item')
    def __reduce_ex__(self, *args, **kwargs):
        return self._item.__reduce_ex__(*args, **kwargs)

    @instance_shared_sync('item')
    def __hash__(self):
        return self._item.__hash__()

    @instance_shared_sync('item')
    def __format__(self, *args, **kwargs):
        return self._item.__format__(*args, **kwargs)

    @instance_shared_sync('item')
    def __reduce__(self, *args, **kwargs):
        return self._item.__reduce__(*args, **kwargs)

    @instance_shared_sync('item')
    def __sizeof__(self):
        return self._item.__sizeof__()

    @instance_shared_sync('item')
    def __str__(self):
        return self._item.__str__()

    @instance_shared_sync('item')
    def __delattr__(self, name):
        return self._item.__delattr__(name)

    @instance_shared_sync('item')
    def __repr__(self):
        return self._item.__repr__()

if __name__ == '__main__':

    @async
    def f():
        for x in range(10000):
            print(x)

    def g():
        print("Done")

    t = f()
    t.done += g

    for x in range(10000,20000):
        print(x)

    t.join()

    i = 5

    @safeAsync
    @debug.trace()
    def unsafe():
        global i
        i -= 1
        print(i)
        if i > 0:
            raise Exception

    unsafe()

