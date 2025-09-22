import networkx as nx
import matplotlib.pyplot as plt

def load_file(path):
    with open(path, "r") as f:
        doc = f.read()
    return doc

def get_ants(doc):
    return doc.splitlines()[0]

def get_connections(doc):
    connections: list[str] = []
    for line in doc.splitlines()[1:]:
        if "-" in line:
            connections.append(line)
    return connections

def build_graph(connections):
    nodes = _get_node_length(connections)
    end = len(nodes) - 1
    G = nx.DiGraph()
    for connection in connections:
        node1, node2 = connection.split(" - ")
        G.add_edge(node1, node2)

    pos = {
        "Sv": (0, 0),
        "Sd": (end, 0)
    }

    options = dict(
        with_labels=True,
        node_size=1500,
        node_color="lightblue",
        arrowsize=20,
        font_size=12
    )

    return (G, pos, options)

def _get_node_length(connections):
    nodes = set()
    for connection in connections:
        term = connection.split(" ")  # ['Sv','-','S1']
        term.pop(1)                   # ['Sv','S1']
        nodes.update(term)            # ajoute les deux éléments au set
    return nodes

if __name__ == "__main__":
    doc = load_file("fourmilieres/fourmiliere_zero.txt")
    connections = get_connections(doc)
    print(_get_node_length(connections))
    nx.draw_networkx(*build_graph(connections))