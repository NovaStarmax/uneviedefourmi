import networkx as nx

class Anthill: 
    def __init__(self, rooms, tunnels, capacities):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(rooms)
        self.graph.add_edges_from(tunnels)
        self.capacities = capacities


def _parse_anthill(file: str) -> list :
    with open(file, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def initialize_anthill(file: str): 
    lines = _parse_anthill(file)
    nb_ants = 0
    rooms = set()
    tunnels = []
    capacities = {}

    for l in lines:
        if l.startswith("f="):
            nb_ants = int(l.split("=")[1])
        elif "-" in l:
            a, b = [x.strip() for x in l.split("-")]
            tunnels.append((a, b))
            rooms.add(a); rooms.add(b)
        elif "{" in l:
            id_room = l.split("{")[0].strip() 
            capacity = int(l.split("{")[1].replace("}", "").strip()) 
            rooms.add(id_room)
            capacities[id_room] = capacity
        else:
            rooms.add(l)

    for s in ["Sv", "Sd"]: # vestibule et dortoir = capacité nb_ants
        rooms.add(s)
        capacities[s] = nb_ants

    for s in rooms: # par défaut, capacité = 1
        capacities.setdefault(s, 1)
    return nb_ants, list(rooms), tunnels, capacities

def is_valid_room(room, ants, capacity) -> bool:
    occupied = sum(f.position == room for f in ants)
    return occupied < capacity

def get_steps_paths(anthill, ants):
    steps = []
    while any(f.position != "Sd" for f in ants):
        movements = []
        for f in ants: 
            if f.position == "Sd":
                continue
            path = nx.shortest_path(anthill.graph, f.position, "Sd")
            if len(path) >= 2:
                next_room=path[1]
                if is_valid_room(next_room,ants,anthill.capacities[next_room]):
                    movements.append(f"{f.name}_{f.id}-{f.position}-{next_room}")
                    f.position = next_room
        steps.append(movements)
    return steps