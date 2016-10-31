'''
 Graphing Components
'''

class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_node(self, node, weight):
        self.edges[node.name] = Edge(self, node, weight)
        return self
