'''
 DAG Path Finder
'''

from .paths import SingleSource
from .utils import get_topological_order


class DAG(SingleSource):
    def find_path(self):
        order = get_topological_order(self.graph)
        for src in order:
            for dest, edge in self.graph[src].edges.items():
                if self.D[src] + edge.weight < self.D[dest]:
                    self.D[dest] = self.D[src] + edge.weight
        return self.D
