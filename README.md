# Une vie de fourmi

Cette application simule les déplacements de fourmis au sein d'une fourmilière modélisée comme un graphe. Les chemins optimaux sont calculés avec NetworkX et une animation Matplotlib illustre l'avancée des fourmis, en appliquant les contraintes de capacité propres à chaque salle.

## Fonctionnalités
- Lecture d'une configuration de fourmilière décrivant salles, tunnels et capacités.
- Attribution de chemins courts aux fourmis tout en respectant le nombre maximal d'individus par salle.
- Visualisation animée pas à pas des déplacements sur un graphe NetworkX.
- Génération de noms de fourmis pour un suivi plus lisible dans la console et sur l'animation.

## Installation
Prerequis : Python 3.11 ou supérieur.

1. Créez et activez un environnement virtuel si souhaité.
2. Installez les dépendances du projet :
   ```bash
   uv sync
   ```
   ou, à défaut :
   ```bash
   pip install networkx matplotlib ipykernel
   ```

## Lancer la simulation
1. Exécutez `uv run main.py`.
2. Choisissez l'une des fourmilières proposées (0 à 5). Les fichiers correspondants se trouvent dans `fourmiliere/`.
3. Le script affiche dans la console les positions des fourmis à chaque étape, puis ouvre une fenêtre Matplotlib montrant les déplacements sur le graphe.

## Structure du projet
- `main.py` : point d'entrée. Charge la fourmilière choisie, instancie les fourmis, calcule leurs trajets avec `get_steps_paths` et lance l'animation Matplotlib.
- `anthill.py` : définit la classe `Anthill`, le parseur des fichiers texte, ainsi que la logique d'assignation des chemins et des mouvements étape par étape.
- `ants.py` : classe `Ants` représentant une fourmi (identifiant, nom, position courante).
- `anthill_choice.py` : invite l'utilisateur à sélectionner un fichier de fourmilière et renvoie le chemin correspondant.
- `name_generator.py` : fournit des noms uniques et humoristiques aux fourmis pour faciliter le suivi.
- `txt_to_graph.py` : utilitaire pour charger un fichier de fourmilière, construire un graphe dirigé et le visualiser dans un but d'exploration.
- `plot_graph.ipynb` : notebook Jupyter pour expérimenter autour de la représentation graphique des fourmilières.
- `fourmiliere/` : dossiers textes utilisés par l'application. Chaque fichier décrit une topologie de fourmilière.
- `fourmilieres/` : variantes de fichiers de configuration (non utilisés par défaut mais conservés pour référence).
- `pyproject.toml` : métadonnées du projet et liste des dépendances nécessaires à l'installation.

## Format d'un fichier de fourmilière
Chaque fichier `.txt` suit le format suivant :
- `f=<nombre>` : nombre total de fourmis à générer.
- Lignes avec un identifiant seul (`S1`, `SalleA`, etc.) : déclaration d'une salle avec la capacité par défaut (1 fourmi).
- Lignes `Salle{capacité}` : déclarations explicites de capacité, par exemple `SalleA{3}` autorise trois fourmis simultanées.
- Lignes `SalleX - SalleY` : tunnels bidirectionnels entre deux salles.
- Les salles spéciales `Sv` (salle de départ) et `Sd` (salle d'arrivée) sont ajoutées automatiquement avec une capacité égale au nombre de fourmis.

## Personnalisation
- Ajoutez de nouveaux fichiers dans `fourmiliere/` en respectant le format ci-dessus pour créer d'autres topologies.
- Ajustez la constante `max_paths` de `get_steps_paths` dans `anthill.py` pour modifier le nombre de trajets distincts pris en compte.
- Modifiez `name_generator.NAMES` si vous souhaitez enrichir la liste de noms disponibles.

## Dépannage
- Si aucune fenêtre ne s'ouvre, vérifiez que votre environnement Python dispose d'un backend Matplotlib compatible (par exemple `pip install matplotlib[qt]` sur certaines plateformes).
- En cas de `ValueError` lors du choix de la fourmilière, assurez-vous d'entrer un chiffre entre 0 et 5.
