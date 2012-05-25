__author__ = 'David'

from heapq import heappop, heappush

class Simulator:

    def __init__(self):
        self.events = []
        self.beforeEvent = []
        self.afterEvent = []
        self.timeSpent = 0
        self.totalEvents = 0

    def SetInitialEvents(self,init_events):
        self.events = []
        self.timeSpent = 0
        self.totalEvents = 0
        self.InsertEvents(init_events)

    def InsertEvents(self, events):
        if events == None: return
        for e in events:
            if e.time>=self.timeSpent:
                heappush(self.events,e)

    def __processNextEvent(self):
        e = heappop(self.events)
        t = e.time
        for m in self.beforeEvent: m(self,e)
        self.InsertEvents(e.Process())
        self.totalEvents+=1
        self.timeSpent = t
        for m in self.afterEvent: m(self,e)

    def Simulate(self, time = None, untilTime=None, events=None, untilEvent=None):
        start_time= self.timeSpent
        first_event = self.totalEvents
        while   len(self.events)!=0 and\
                (time==None or self.events[0][0]-start_time<=time) and\
                (untilTime==None or self.events[0][0]<=untilTime)and\
                (events == None or self.totalEvents-first_event<events) and\
                (untilEvent==None or self.totalEvents<untilEvent):
            self.__processNextEvent()

        if len(self.events)!=0 and\
           (events == None or self.totalEvents-first_event<events) and\
           (untilEvent==None or self.totalEvents<untilEvent):
            if time!=None and self.events[0][0]-start_time> time >= 0:
                self.timeSpent = start_time + time
            elif untilTime!=None and self.events[0][0]> untilTime > self.timeSpent:
                self.timeSpent = untilTime

        return len(self.events)!=0