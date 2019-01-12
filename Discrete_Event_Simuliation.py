# 通过标准库模拟出租车运营的离散事件仿真
import collections
import random
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAIX = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5
Event = collections.namedtuple('Event',['time', 'porc', 'action'])




def taxi_process(ident, trips, start_time = 0):
    '''taix实例'''
    time = yield Event(start_time, ident, "leave garage")
    for i in range(trips):
        time = yield Event(time, ident, "pick up passenger")
        time = yield Event(time, ident, "drop off passenger")
    yield Event(time, ident, "going home")


def compute_duration(previous_action):
    if previous_action in ["leave garage", "drop off passenger"]:
        interval = SEARCH_DURATION      #如果为出库或送到，下一个状态为寻找乘客
    elif previous_action == "pick up passenger":
        interval = TRIP_DURATION        #如果为pick up则状态为运送乘客
    elif previous_action == "going home":
        interval = 1
    else:
        raise ValueError("Unknown previous_actions:%s" % previous_action)
    return int(random.expovariate(1/interval)) + 1

class Simulator(object):
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, stoptime):
        simtime = 0
        for _, proc in sorted(self.procs.items()):
            self.events.put(proc.__next__())

        while simtime < stoptime:
            if self.events.empty():
                print("END OF EVENTS")
                break
            current = self.events.get()
            simtime, proc, action = current
            print("taix:", proc, proc*" ", current)
            try:
                next_event = self.procs[proc].send(simtime + compute_duration(action))
            except StopIteration as exc:
                self.procs.pop(proc)
            else:
                self.events.put(next_event)
        else:
            print("END OF SIMULATION TIME : {} EVENTS PENDING",format(self.events.qsize()))

