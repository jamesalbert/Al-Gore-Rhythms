
'''
 Bellman-Ford Shortest Path Finder
'''

from .paths import SingleSource


class BellmanFord(SingleSource):
    def find_path(self, q=None):
        if q == None:
            q = [self.source]
        for src in q:
            for dest, edge in self.graph[src].edges.items():
                if self.D[src] + edge.weight < self.D[dest]:
                    self.D[dest] = self.D[src] + edge.weight
            self.find_path(q=self.graph[src].edges.keys())
        return self.D
