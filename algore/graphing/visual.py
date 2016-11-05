import networkx as nx
import matplotlib.pyplot as plt
import pylab
from .utils import rollout


def draw(datamap):
    g = nx.DiGraph()
    edges = rollout(datamap)
    for edge in edges:
        src, dest, weight = edge
        g.add_edge(src, dest, weight=weight)
    pos = nx.circular_layout(g)
    edge_labels = dict([((u, v,), d['weight'])
                       for u, v, d in g.edges(data=True)])
    node_labels = {node: node for node in g.nodes()}
    nx.draw_networkx_labels(g, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    nx.draw(g, pos, node_size=500, edge_cmap=plt.cm.Reds)
    pylab.show()
