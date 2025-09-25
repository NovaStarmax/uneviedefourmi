from itertools import cycle
import networkx as nx
import matplotlib.pyplot as plt

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

def is_valid_room(room, ants, capacity):
    # compte combien de fourmis sont déjà dans la salle
    occupied = sum(1 for f in ants if f.position == room)
    return occupied < capacity

def get_steps_paths(anthill, ants, max_paths=5):
    all_paths = list(nx.shortest_simple_paths(anthill.graph, "Sv", "Sd"))
    if len(all_paths) > max_paths:
        all_paths = all_paths[:max_paths]

    assignments = {}
    for i, ant in enumerate(ants):
        assignments[ant] = all_paths[i % len(all_paths)]

    steps = []
    while any(f.position != "Sd" for f in ants):
        movements = []
        # Pour chaque étape, on re-calcule la salle occupée pour vérifier la capacité
        occupied_rooms = {room: 0 for room in anthill.capacities.keys()}
        for f in ants:
            if f.position != "Sd":
                occupied_rooms[f.position] += 1

        for ant in ants:
            if ant.position == "Sd":
                continue
            path = assignments[ant]
            if ant.position not in path:
                ant.position = path[0]
                movements.append(f"{ant.name}_{ant.id}-{ant.position}-{ant.position}")
                continue
            pos_index = path.index(ant.position)
            next_room = None
            if pos_index + 1 < len(path):
                candidate = path[pos_index + 1]
                # Vérifier capacité et présence dans occupied_rooms
                if occupied_rooms[candidate] < anthill.capacities[candidate]:
                    next_room = candidate

            if next_room:
                movements.append(f"{ant.name}_{ant.id}-{ant.position}-{next_room}")
                occupied_rooms[ant.position] -= 1
                occupied_rooms[next_room] += 1
                ant.position = next_room
            else:
                movements.append(f"{ant.name}_{ant.id}-{ant.position}-{ant.position}")

        steps.append(movements)

    return steps