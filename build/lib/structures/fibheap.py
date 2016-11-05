
from heapq import heappush, heappop

class FibonacciHeap(object):
    def __init__(self):
        self.h = []
        self.min = None

    def min(self):
        return self.min

    def link(self, x, y):
        heappop(self.h, x)
        i  = self.h.index(y)
        self.h.insert(2*i+2, x)
