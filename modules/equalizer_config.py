# modules/equalizer_config.py

# === Limites de gain pour chaque bande ===
EQUALIZER_LIMITS = {
    "bass": (-10, 10),
    "mid": (-10, 10),
    "treble": (-10, 10),
}

# === Valeurs par défaut à l'initialisation ===
DEFAULT_EQUALIZER = {
    "bass": 0,
    "mid": 0,
    "treble": 0,
}

# === Ordre d'affichage des bandes (interface graphique) ===
EQUALIZER_BANDS = ["bass", "mid", "treble"]

# === Nom du fichier de configuration JSON utilisé ===
CONFIG_FILE = "config.json"
