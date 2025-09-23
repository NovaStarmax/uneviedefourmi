# ants.py
import networkx as nx

class Fourmiliere:
    """
    Graphe représentant la fourmilière.
    """
    def __init__(self, salles, tunnels, capacites):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(salles)
        self.graph.add_edges_from(tunnels)
        self.capacites = capacites

class Fourmi:
    def __init__(self, id, position):
        self.id = id
        self.position = position

def est_libre(salle, fourmis, capacite):
    """
    Retourne True si la salle a encore de la place (occupee < capacite).
    """
    occupee = sum(1 for f in fourmis if f.position == salle)
    return occupee < capacite

def deplacer_fourmis(fourmiliere, fourmis, vestibule, dortoir, max_steps=10000):
    """
    Déplace les fourmis du vestibule au dortoir.
    - Utilise le plus court chemin (NetworkX) pour chaque fourmi.
    - Retourne une liste d'étapes; chaque étape est une liste de chaînes
      "f{id} - ancien - nouveau" des mouvements effectués pendant l'étape.
    - Stoppe si aucune fourmi ne peut bouger (impasse) ou si max_steps dépassé.
    """
    étapes = []
    step = 0

    while any(f.position != dortoir for f in fourmis):
        step += 1
        mouvements = []

        # itération déterministe par id
        for f in sorted(fourmis, key=lambda x: x.id):
            if f.position == dortoir:
                continue

            # essayer de trouver un chemin vers le dortoir
            try:
                chemin = nx.shortest_path(fourmiliere.graph, f.position, dortoir)
            except nx.NetworkXNoPath:
                continue

            if len(chemin) < 2:
                continue

            suivant = chemin[1]
            # capacité connue (sécurité : .get)
            cap = fourmiliere.capacites.get(suivant, 1)

            # Si la salle suivante est le dortoir on laisse entrer (cap testé aussi),
            # sinon on n'y va que si est_libre == True
            if suivant == dortoir or est_libre(suivant, fourmis, cap):
                ancien = f.position
                f.position = suivant
                mouvements.append(f"f{f.id} - {ancien} - {suivant}")

        if not mouvements:
            print("Aucun mouvement possible (impasse détectée). Arrêt.")
            break

        étapes.append(mouvements)

        if step >= max_steps:
            print("Nombre maximum d'étapes atteint, arrêt pour sécurité.")
            break

    return étapes
