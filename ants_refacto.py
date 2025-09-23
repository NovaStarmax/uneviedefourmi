import networkx as nx

class Anthill: 
    def __init__(self, rooms, tunnels, capacites):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(rooms)
        self.graph.add_edges_from(tunnels)
        self.capacites = capacites

