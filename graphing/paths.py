'''
 Subclass for single-source shortest path finders
'''

from .utils import infinity


class PathFinder(object):
    def __init__(self, graph, v):
        self.graph = graph
        self.v = v
        self.D = {v: 0}
        for vertex in self.graph.keys():
            if self.v == vertex:
                continue
            self.D[vertex] = infinity

    def find_path(self):
        raise NotImplementedError
