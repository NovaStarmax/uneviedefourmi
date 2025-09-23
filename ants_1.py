import networkx as nx

class Fourmiliere:
    def __init__(self, salles, tunnels, capacites):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(salles)
        self.graph.add_edges_from(tunnels)
        self.capacites = capacites

class Fourmi:
    def __init__(self, id):
        self.id = id
        self.position = "Sv"

def lire_fourmiliere(fichier):
    """
    Lit un fichier texte et retourne (nb_fourmis, salles, tunnels, capacites).
    """
    with open(fichier, encoding="utf-8") as f:
        lignes = [l.strip() for l in f if l.strip()]  # mettre dans une autre fonction

    nb_fourmis = 0
    salles = set()
    tunnels = []
    capacites = {}

    for l in lignes:
        if l.startswith("f="):
            nb_fourmis = int(l.split("=")[1])
        elif "-" in l:
            a, b = [x.strip() for x in l.split("-")]
            tunnels.append((a, b))
            salles.add(a); salles.add(b)
        elif "{" in l:
            nom = l.split("{")[0].strip() #wtf
            cap = int(l.split("{")[1].replace("}", "").strip()) #wtf
            salles.add(nom)
            capacites[nom] = cap
        else:
            salles.add(l)

    # vestibule et dortoir = capacité nb_fourmis
    for s in ["Sv", "Sd"]:
        salles.add(s)
        capacites[s] = nb_fourmis

    # par défaut, capacité = 1
    for s in salles:
        capacites.setdefault(s, 1)

    return nb_fourmis, list(salles), tunnels, capacites

def est_libre(salle, fourmis, capacite):
    occupee = sum(f.position == salle for f in fourmis)
    return occupee < capacite

def deplacer_fourmis(fourmiliere, fourmis):
    """
    Déplace les fourmis de Sv vers Sd et retourne les étapes.
    """
    etapes = []
    while any(f.position != "Sd" for f in fourmis):
        mouvements = []
        for f in fourmis:
            if f.position == "Sd":
                continue
            chemin = nx.shortest_path(fourmiliere.graph, f.position, "Sd")
            if len(chemin) >= 2:
                next_room = chemin[1]
                if est_libre(next_room, fourmis, fourmiliere.capacites[next_room]):
                    mouvements.append(f"f{f.id} - {f.position} - {next_room}")
                    f.position = next_room
        etapes.append(mouvements)
    return etapes
