'''
 Graphing Components
'''

from collections import MutableMapping
from copy import copy
from itertools import zip_longest


class Graph(MutableMapping):
    def __init__(self, datamap, directed):
        self.datamap = datamap
        self.directed = directed
        self.graph = {}

    def get_vertices(self):
        return list(self.graph.values())

    def get_vertice_names(self):
        return sorted(list(self.graph.keys()))

    def get_edges(self):
        edges = {}
        for vertex in self.get_vertices():
            src = vertex.name

            edges = {
                **edges, **{
                    '{0}_{1}'.format(src, dest): edge
                    for dest, edge in vertex.edges.items()
                }
            }
        return edges

    def add_vertex(self, name):
        self[name] = Vertex(name)
        return self

    def remove_vertex(self, vertex):
        incoming_from = vertex.get_incoming()
        outgoing_to = vertex.get_outgoing()
        for incoming, outgoing in zip_longest(incoming_from, outgoing_to):
            if incoming:
                self.remove_edge(self[incoming].edges[vertex.name])
            if outgoing:
                self.remove_edge(vertex.edges[outgoing])
        self.graph.pop(vertex.name, None)
        return self

    def add_edge(self, src, dest, weight):
        edge = Edge(self.graph[src], self.graph[dest], weight)
        return self._connect(src, dest, edge)

    def remove_edge(self, edge):
        src = edge.source.name
        dest = edge.destination.name
        if src in self.graph[dest].edges:
            self._disconnect(dest, src)
        return self._disconnect(src, dest)

    def _connect(self, src, dest, edge):
        self.graph[src].edges[dest] = edge
        self.graph[src].outgoing_to.append(dest)
        self.graph[dest].incoming_from.append(src)
        return self

    def _disconnect(self, src, dest):
        self.graph[src].edges.pop(dest)
        self.graph[src].outgoing_to.remove(dest)
        self.graph[dest].incoming_from.remove(src)
        return self

    def __contains__(self, item):
        return item in self.graph

    def __getitem__(self, key):
        return self.graph[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.graph[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.graph[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.graph)

    def __len__(self):
        return len(self.graph)

    def __keytransform__(self, key):
        return key


class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.edges = {}
        self.incoming_from = []
        self.outgoing_to = []

    def has_incoming_edges(self):
        return not not self.incoming_from

    def get_incoming(self):
        return copy(self.incoming_from)

    def get_outgoing(self):
        return copy(self.outgoing_to)
