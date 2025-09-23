from ants_1 import Fourmiliere, Fourmi, lire_fourmiliere, deplacer_fourmis
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == "__main__":
    fichier = "fourmiliere/fourmiliere_quatre.txt"

    nb_fourmis, salles, tunnels, capacites = lire_fourmiliere(fichier)

    print("Nb fourmis :", nb_fourmis)
    print("Salles :", salles)
    print("Tunnels :", tunnels)
    print("Capacités :", capacites)

    # construction
    f = Fourmiliere(salles, tunnels, capacites)
    fourmis = [Fourmi(i+1) for i in range(nb_fourmis)]

    # déplacements
    etapes = deplacer_fourmis(f, fourmis)

    # affichage console
    for i, e in enumerate(etapes, 1):
        print(f"\n+++ E{i} +++")
        for m in e:
            print(m)

    # affichage graphe
    pos = nx.spring_layout(f.graph, seed=42)
    nx.draw(f.graph, pos, with_labels=True, node_color="lightblue")
    plt.title("Structure de la fourmilière")
    plt.show()
