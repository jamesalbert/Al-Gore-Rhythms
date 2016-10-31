'''
 Graphing Utilities
'''

from .components import Vertex

infinity = 10000000

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
    graph = {}
    edges = rollout(datamap)
    for edge in edges:
        src, dest, weight = edge
        if src not in graph:
            graph[src] = Vertex(src)
        if dest not in graph:
            graph[dest] = Vertex(dest)
        if not directed:
            graph[dest].add_node(graph[src], weight)
        graph[src].add_node(graph[dest], weight)
    return graph
