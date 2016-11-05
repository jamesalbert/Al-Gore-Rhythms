'''
 Kruskal Shortest Path Finder
'''

from .paths import MinimumSpanning


class Kruskal(MinimumSpanning):
    def get_path(self, t, current=None):
        current = current or self.source
        if current == self.destination:
            return str()
        vertex = self.graph[current]
        edges = [edge for edge in vertex.edges.values() if edge in t]
        current = min(edges, key=lambda edge: edge.weight).destination.name
        return current + self.get_path(t, current)

    def find_path(self):
        q = self.graph.get_edges()
        t = []
        c = {}
        for vertex in self.graph.get_vertices():
            c[vertex.name] = [vertex]
        while len(t) < len(self.graph) - 1:
            edge = min(q.values(), key=lambda edge: edge.weight)
            src = edge.source.name
            dest = edge.destination.name
            q.pop('{0}_{1}'.format(src, dest))
            if c[src] is not c[dest]:
                t.append(edge)
                c[dest] += c[src]
                c[src] = c[dest]
        return self.get_path(t)
