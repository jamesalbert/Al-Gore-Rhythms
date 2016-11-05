'''
 Graphing Utilities
'''

from .components import Graph


infinity = 10000000


def get_topological_order(graph):
    order = list()
    graph_bk = read_datamap(graph.datamap, directed=True)
    vertices = graph_bk.get_vertices()
    while len(order) < len(vertices):
        for vertex in vertices:
            if vertex.name in order:
                continue
            if not vertex.has_incoming_edges():
                order.append(vertex.name)
                graph_bk.remove_vertex(vertex)
    return order


def rollout(datamap):
    '''
     converts datamap ( {'a': {'b': 12}} ) to [ ['a', 'b', 12] ]
    '''
    digraph = []
    for src, edges in datamap.items():
        for dest, weight in edges.items():
            digraph.append([src, dest, weight])
    return digraph


def read_datamap(datamap, directed=False):
    '''
     constructs a map of vectors and associated edges from a datamap
    '''
    graph = Graph(datamap, directed)
    edges = rollout(datamap)
    for edge in edges:
        src, dest, weight = edge
        if src not in graph:
            graph.add_vertex(src)
        if dest not in graph:
            graph.add_vertex(dest)
        if not directed:
            graph.add_edge(dest, src, weight)
        graph.add_edge(src, dest, weight)
    return graph
