# ant_names.py
import random

NAMES = [
    "fourmiznator", "ant_man", "la_foumi_fatale", "general_sixpattes", "el_hormigon",
    "tiny_terminator", "fourmibuster", "la_piquante", "colonel_antastic", "senor_mandibula",
    "lady_mandibule", "captain_miette", "el_chiquito", "la_cracotte", "major_moustache",
    "reine_chaussette", "docteur_antipasti", "fourmiricain", "sergent_tapas", "la_fourmi_ninja",
    "madame_biscotte", "don_fourmillo", "antastique_voyageur", "le_ronge_cable", "senorita_antena",
    "professeur_minuscule", "fourmidable_hulk", "la_casse_croute", "senor_piquante", "ant_manuel_valls",
    "la_fourmizeria", "colonel_cucaracha", "la_micro_machine", "don_crumble", "miss_sixpattes",
    "inspector_fourmiga", "jean_luc_mandibule", "antoine_fourmi", "el_minusculo", "le_croque_sucre",
    "general_biscuit", "senor_chipotle", "la_fourmichouette", "doctor_six_legs", "la_morfale",
    "el_hormiguero", "soeur_fourmiette", "big_boss_micro", "la_fourmizilla", "comandante_crumb"
]

_stock = random.sample(NAMES, k=len(NAMES))

def get_ant_name() -> str:
    if not _stock:
        raise RuntimeError("No names remaining")
    return _stock.pop()