import os
import json

# Chemin du fichier de configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")

# Configuration par défaut
DEFAULT_CONFIG = {
    "theme": "dark",
    "brightness": 75,
    "volume": {
        "output1": 70,
        "output2": 70,
        "output3": 70
    },
    "split_mode": {
        "output1": "stereo",
        "output2": "stereo",
        "output3": "stereo"
    },
    "equalizer": {
        "bass": 0,
        "mid": 0,
        "treble": 0
    },
    "rtc_time": "auto"
}

def load_config():
    """Charge le fichier de configuration, ou crée le fichier par défaut."""
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[SystemConfig] Erreur de lecture config.json : {e}")
        return DEFAULT_CONFIG

def save_config(config):
    """Sauvegarde la configuration dans le fichier JSON."""
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"[SystemConfig] Erreur de sauvegarde config.json : {e}")

def get_value(key_path):
    """Récupère une valeur par chemin (ex: volume.output1)."""
    keys = key_path.split(".")
    config = load_config()
    for key in keys:
        config = config.get(key, {})
    return config

def set_value(key_path, value):
    """Modifie une valeur par chemin et sauvegarde."""
    keys = key_path.split(".")
    config = load_config()
    sub_config = config
    for key in keys[:-1]:
        sub_config = sub_config.setdefault(key, {})
    sub_config[keys[-1]] = value
    save_config(config)
