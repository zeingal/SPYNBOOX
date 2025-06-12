# modules/equalizer_config.py

# Limites de gain pour chaque bande
EQUALIZER_LIMITS = {
    "bass": (-10, 10),
    "mid": (-10, 10),
    "treble": (-10, 10),
}

# Valeurs par défaut au démarrage
DEFAULT_EQUALIZER = {
    "bass": 0,
    "mid": 0,
    "treble": 0,
}

# Liste ordonnée pour l'affichage
EQUALIZER_BANDS = ["bass", "mid", "treble"]
