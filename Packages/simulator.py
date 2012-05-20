# -*- coding: utf8 -*-

__author__ = 'David'

from heapq import heappop, heappush

class Simulator:

    def __init__(self):
        self.events = []
        self.before_event = []
        self.after_event = []
        self.time_spent = 0
        self.total_events = 0

    def SetInitialEvents(self,init_events):
        self.events = []
        self.time_spent = 0
        self.total_events = 0
        self.InsertEvents(init_events[:])

    def InsertEvents(self, events):
        if events == None: return
        for e in events:
            if e.time>=self.time_spent:
                heappush(self.events,(e.time,e))

    def __processNextEvent(self):
        t,e = heappop(self.events)
        for m in self.before_event: m(self,e)
        self.InsertEvents(e.process())
        for m in self.after_event: m(self,e)
        self.total_events+=1
        self.time_spent = t

    def Simulate(self,time = None,until_time=None,events=None,until_event=None):
        start_time= self.time_spent
        first_event = self.total_events
        while   len(self.events)!=0 and\
                (time==None or self.events[0][0]-start_time<=time) and\
                (until_time==None or self.events[0][0]<=until_time)and\
                (events == None or self.total_events-first_event<events) and\
                (until_event==None or self.total_events<until_event):
            self.__processNextEvent()

        if len(self.events)!=0 and\
           (events == None or self.total_events-first_event<events) and\
           (until_event==None or self.total_events<until_event):
            if time!=None and self.events[0][0]-start_time> time >= 0:
                self.time_spent = start_time + time
            elif until_time!=None and self.events[0][0]> until_time > self.time_spent:
                self.time_spent = until_time

        return len(self.events)!=0
