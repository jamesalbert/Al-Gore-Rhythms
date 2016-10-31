'''
 Dijkstra Shortest Path Finder
'''

from .paths import PathFinder


class Dijkstra(PathFinder):
    def find_path(self):
        q = list(self.graph.keys())
        while q:
            src = min(q, key=self.D.get)
            q.pop(q.index(src))
            for dest, edge in self.graph[src].edges.items():
                if dest not in q:
                    continue
                if self.D[src] + edge.weight < self.D[dest]:
                    self.D[dest] = self.D[src] + edge.weight
        return self.D
