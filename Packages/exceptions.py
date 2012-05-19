"""
Define las excepciones locales.
"""

import types
import sys
import debug

class _Exception(object):
    def __init__(self, exc = None, trace = None):
        self.exc = exc
        self.trace = trace

    def throw(self):
        raise self.exc

    def __eq__(self, other):
        return isinstance(other, _ExceptionSingleton)

    def __nonzero__(self):
        return False


class _ExceptionSingleton(object):
    pass

EXCEPTION = _ExceptionSingleton()


class ExceptionCatcher(object):
    def __init__(self, instance):
        self._instance = instance

    def __safeInvoke(self, function, *args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            trace = sys.exc_traceback
            e.stack_trace = trace
            exc = _Exception(e, trace)
            debug.error(function, e, throw=False)
            return exc

    def __getattr__(self, item):
        attr = getattr(self._instance, item)

        if type(attr) == types.MethodType or type(attr) == types.FunctionType:
            def decorator(callable):
                def function(*args, **kwargs):
                    return self.__safeInvoke(attr, *args, **kwargs)
                return function
            return decorator(attr)
        else:
            return attr

    def __getitem__(self, item):
        getitem = self._instance.__getitem__
        return self.__safeInvoke(getitem, item)
