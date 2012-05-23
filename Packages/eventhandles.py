# -*- coding: utf8 -*-

""" Funcionalidades para permitir eventos .net-like
"""

import debug

class EventHandler(object):
    def __init__(self, name, once: False):
        self.callables = []
        self.name = name
        self.once = once
        self.calls = 0

    def __repr__(self):
        return "<EventHandler '{0}' ({1} callbacks)>".format(self.name, len(self.callables))

    @debug.trace('tools.events.private')
    def __add__(self, other):
        if isinstance(other, tuple):
            args = other[1]
            call = other[0]
        else:
            args = tuple()
            call = other

        if not hasattr(call, "__call__"):
            raise Exception("Not a callable {0}".format(other))

        debug.debug("Adding callback {0}", call.__name__, category = 'tools.events.private')
        self.callables.append((call, args))

        if self.once and self.calls > 0:
            debug.debug("Calling callback after invoke.")
            self(self.args, self.kwargs)

        return self

    @debug.trace('tools.events.private')
    def __sub__(self, call):
        if not hasattr(call, "__call__"):
            raise Exception("Not a callable {0}".format(call))

        self.callables.remove(call)
        return self

    @debug.trace('tools.events.private')
    def __call__(self, *args, **kwargs):
        self.calls += 1

        if self.once and self.calls > 1:
            debug.warning("Calling event {0} declared as 'once' multiple ({1}) times.", (self, self.calls))

        if not self.callables:
            debug.debug("No callbacks submited", category = 'tools.events.private')

        for c, t in self.callables:
            t = tuple(t + args)

            debug.debug("Executing event callback {0} with args {1}", (c.__name__, (t, kwargs)),
                        category = 'tools.events.private')

            c(*t, **kwargs)

        self.args = args
        self.kwargs = kwargs


class Event(object):
    def __init__(self, name = None, once = False):
        self.name = name
        self.once = once

    def __repr__(self):
        return "<Event '{0}'>".format(self.name)

    @debug.trace('tools.events.private')
    def __get__(self, instance, owner):
        field = '{0}_event_handler'.format(self.name)

        if instance:
            if not hasattr(instance, field):
                debug.debug("Adding {0} field to instance", field, category = 'tools.events.private')
                setattr(instance, field, EventHandler(self.name, self.once))

            return getattr(instance, field)
        else:
            if not hasattr(owner, field):
                debug.debug("Adding {0} field to class", field, category = 'tools.events.private')
                setattr(owner, field, EventHandler(self.name, self.once))

            return getattr(owner, field)


    @debug.trace('tools.events.private')
    def __set__(self, instance, value):
        field = '{0}_event_handler'.format(self.name)

        if isinstance(value, EventHandler):
            setattr(instance, field, value)
        else:
            setattr(instance, field, EventHandler(self.name, self.once) + value)

    @debug.trace('tools.events.private', level = debug.ERROR)
    def __call__(self, *args, **kwargs):
        raise Exception("You should not be calling this.")


if __name__ == '__main__':
# Run a small test-case

    class A:
        done = Event('done')

        def __init__(self, x):
            self.x = x

        def f(self):
            print('A.f')
            print(self.x)
            self.done()

    class B(A):
        def __init__(self, x):
            A.__init__(self, x)

        def f(self):
            print('B.f')
            print(self.x)
            self.done()

    def g():
        print('g')

    def h():
        print('h')

    def i():
        print('i')

    a = A(1)
    a.done += g
    a.done += h

    a.f()

    b = B(2)
    b.done += g
    b.done += h

    b.f()

    c = B(3)

    c.done += g

    c.f()

    B.done += i

    A.done()
    B.done()
