from anthill import Anthill, get_steps_paths, initialize_anthill
from ants import Ants
import matplotlib.pyplot as plt
import networkx as nx
from anthill_choice import get_anthill
from name_generator import get_ant_name

if __name__ == "__main__":
    anthill = get_anthill()
    nb_ants, rooms, tunnels, capacities =  initialize_anthill(anthill)
    
    print("Nb ants :", nb_ants)
    print("Rooms :", rooms)
    print("Tunnels :", tunnels)
    print("Capacities :", capacities)

    # construction
    f = Anthill(rooms, tunnels, capacities)
    ants = [Ants(get_ant_name(), i+1) for i in range(nb_ants)]

    # déplacements
    steps = get_steps_paths(f, ants)

    # affichage console
    for i, e in enumerate(steps, 1):
        print(f"\n+++ E{i} +++")
        for m in e:
            print(m)

    # affichage graphe
    pos = nx.spring_layout(f.graph, seed=42)
    nx.draw(f.graph, pos, with_labels=True, node_color="lightblue")
    plt.title("Structure of the anthill")
    plt.show()
