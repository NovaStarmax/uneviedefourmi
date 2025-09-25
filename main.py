from anthill import Anthill, get_steps_paths, initialize_anthill
from ants import Ants
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
from anthill_choice import get_anthill
from name_generator import get_ant_name  # Utilise bien le générateur de noms fourni

if __name__ == "__main__":
    anthill = get_anthill()
    nb_ants, rooms, tunnels, capacities = initialize_anthill(anthill)

    print("Nb ants :", nb_ants)
    print("Rooms :", rooms)
    print("Tunnels :", tunnels)
    print("Capacities :", capacities)

    f = Anthill(rooms, tunnels, capacities)
    ants = [Ants(get_ant_name(), i+1) for i in range(nb_ants)]
    steps = get_steps_paths(f, ants)  # chaque élément est une liste des positions (noms de salles) des fourmis à l'étape i

    # Affichage console des déplacements par étape
    for i, e in enumerate(steps, 1):
        print(f"\n___ E{i} ___")
        for j, position in enumerate(e):
            print(f"Fourmi {ants[j].name} : {position}")

    # Layout fixe pour la visualisation
    pos = nx.spring_layout(f.graph, seed=42)

    fig, ax = plt.subplots()
    
    def update(frame):
        ax.clear()
        nx.draw(f.graph, pos, ax=ax, with_labels=True, node_color="lightblue")
        current_positions = steps[frame]
        for idx, move in enumerate(current_positions):
            parts = move.split('-')
            ant_position = parts[2] 
            xy = pos[ant_position]
            ax.scatter(*xy, color='red', s=100)
            ax.text(xy[0], xy[1], ants[idx].name, color="black", fontsize=8, ha='center', va='center', backgroundcolor='w')
        ax.set_title(f"Étape {frame + 1}")



    ani = FuncAnimation(fig, update, frames=len(steps), interval=800, repeat=False)
    plt.show()
