# main.py
from ants import Fourmiliere, Fourmi, deplacer_fourmis
import matplotlib.pyplot as plt
import networkx as nx
import re
import os

def lire_fourmiliere(fichier):
    """
    Lit une description de fourmilière depuis un fichier texte.
    Format attendu (exemples) :
      f=10
      S1 { 2 }
      S2
      Sv - S1
      S1 - S2
      S5 - Sd
    Retourne : nb_fourmis, liste_salles, liste_tunnels, dict_capacites
    """
    with open(fichier, encoding="utf-8") as fh:
        raw = fh.read()

    lignes = [l.strip() for l in raw.splitlines() if l.strip() and not l.strip().startswith("#")]

    # récupère f=...
    nb_fourmis = 0
    for l in lignes:
        m = re.match(r"^f\s*=\s*(\d+)", l, re.I)
        if m:
            nb_fourmis = int(m.group(1))
            break

    nodes = set()
    tunnels = []
    capacites = {}

    for l in lignes:
        # ignorer la ligne f=
        if re.match(r"^f\s*=", l, re.I):
            continue

        # tunnel (ligne contenant '-' et pas une définition de capacité)
        if "-" in l and "{" not in l:
            parts = re.split(r"-", l)
            if len(parts) >= 2:
                a = parts[0].strip()
                b = parts[1].strip()
                tunnels.append((a, b))
                nodes.add(a); nodes.add(b)
            continue

        # salle avec capacité : S4 { 2 }
        mcap = re.match(r"^(\S+)\s*\{\s*(\d+)\s*\}$", l)
        if mcap:
            name = mcap.group(1)
            cap = int(mcap.group(2))
            nodes.add(name)
            capacites[name] = cap
            continue

        # simple nom de salle (ex: S1, Sv, Sd)
        if re.match(r'^[A-Za-z0-9_]+$', l):
            nodes.add(l)
            continue

        # sinon on ignore la ligne

    # s'assurer que Sv et Sd existent
    for special in ("Sv", "Sd"):
        if special not in nodes:
            nodes.add(special)
        if special not in capacites:
            # si f renseigné, vestibule/dortoir peuvent contenir toutes les fourmis
            capacites[special] = nb_fourmis if nb_fourmis > 0 else max(1000, len(nodes) * 10)

    # valeurs par défaut (1) pour les autres salles
    for n in nodes:
        if n not in capacites:
            capacites[n] = 1

    return nb_fourmis, sorted(nodes), tunnels, capacites

if __name__ == "__main__":
    # chemin vers le fichier décrivant la fourmilière
    chemin = os.path.join("fourmiliere", "fourmiliere_cinq.txt")  # adapte si nécessaire

    if not os.path.exists(chemin):
        print(f"Fichier non trouvé : {chemin}")
        print("Crée un fichier texte avec la description (ex. la fourmilière de l'énoncé) et relance.")
        raise SystemExit(1)

    nb_fourmis, salles, tunnels, capacites = lire_fourmiliere(chemin)

    print("Fourmilière lue :")
    print("Nombre de fourmis :", nb_fourmis)
    print("Salles :", salles)
    print("Tunnels :", tunnels)
    print("Capacités :", capacites)

    # créer les fourmis (position initiale = Sv)
    fourmis = [Fourmi(i+1, "Sv") for i in range(nb_fourmis)]

    # construire la fourmilière
    f = Fourmiliere(salles, tunnels, capacites)

    # déplacer
    étapes = deplacer_fourmis(f, fourmis, "Sv", "Sd")

    # affichage console des étapes
    for i, e in enumerate(étapes, 1):
        print(f"\n+++ E{i} +++")
        for m in e:
            print(m)

    # affichage du graphe (statique)
    pos = nx.spring_layout(f.graph, seed=42)
    nx.draw(f.graph, pos, with_labels=True, node_color='lightblue')
    plt.title("Structure de la fourmilière")
    plt.show()
