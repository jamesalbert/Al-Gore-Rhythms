from graphing import utils, visual, Dijkstra, BellmanFord

datamap = {
    'a': {
        'b': 10,
        'c': 12
    },
    'b': {
        'c': 20,
        'd': 15,
        'e': 3
    },
    'c': {
        'e': 13,
        'd': 11,
        'f': 17
    },
    'd': {
        'g': 20
    },
    'e': {
        'f': 12,
        'd': 15,
        'g': 12
    },
    'f': {
        'g': 10
    },
    'g': {}
}

# visual.draw(datamap)
undirected = utils.read_datamap(datamap)
directed = utils.read_datamap(datamap, directed=True)
topological_order = utils.get_topological_order(directed)
print('topological order: {0}'.format(topological_order))
d = Dijkstra(undirected, 'a')
b = BellmanFord(directed, 'a')
du = d.find_path()
bu = b.find_path()
# print shortest paths from node 'a' to every other node
print(du)
print(bu)
