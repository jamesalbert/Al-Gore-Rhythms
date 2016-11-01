
from .utils import infinity
from numpy import empty


class AbstractPath(object):
    '''
     Abstract base class for shortest path finders
    '''
    def __init__(self, graph, v):
        self.graph = graph
        self.v = v

    def find_path(self):
        raise NotImplementedError

class SingleSource(AbstractPath):
    '''
     Subclass for single-source shortest path finders
    '''
    def __init__(self, graph, v):
        super().__init__(graph, v)
        self.D = {v: 0}
        for vertex in self.graph:
            if self.v == vertex:
                continue
            self.D[vertex] = infinity


class AllPairs(AbstractPath):
    '''
     Subclass for all-pairs shortest path finders

     these dumb for loops, I hate you Michael and Roberto
    '''
    def __init__(self, graph):
        super().__init__(graph, None)
        vertices = graph.get_vertice_names()
        card = len(vertices)
        self.D = empty((card, card, card), dtype=int)
        for i, v1 in enumerate(vertices):
            for j, v2 in enumerate(vertices):
                if v1 == v2:
                    self.D[0][i][j] = 0
                if v2 in graph[v1].edges:
                    self.D[0][i][j] = graph[v1].edges[v2].weight
                else:
                    self.D[0][i][j] = infinity
        for k in range(1, card):
            for i in range(card):
                for j in range(card):
                    self.D[k][i][j] = min(self.D[k-1][i][j],
                                          self.D[k-1][i][k]+self.D[k-1][k][j])
