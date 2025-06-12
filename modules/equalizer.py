# modules/equalizer.py

import json
import os
from modules.logging import log

CONFIG_FILE = "config.json"

def load_equalizer_settings():
    """
    Charge les réglages de l'égaliseur depuis config.json
    """
    if not os.path.exists(CONFIG_FILE):
        log("Fichier config.json introuvable, valeurs par défaut utilisées.")
        return {"bass": 0, "mid": 0, "treble": 0}

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        eq = config.get("equalizer", {"bass": 0, "mid": 0, "treble": 0})
        return eq
    except Exception as e:
        log(f"Erreur chargement equalizer : {e}")
        return {"bass": 0, "mid": 0, "treble": 0}

def save_equalizer_settings(bass, mid, treble):
    """
    Enregistre les réglages de l'égaliseur dans config.json
    """
    config = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
        except Exception as e:
            log(f"Erreur lecture config pour sauvegarde EQ : {e}")

    config["equalizer"] = {
        "bass": bass,
        "mid": mid,
        "treble": treble
    }

    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        log("Réglages de l’égaliseur enregistrés avec succès.")
    except Exception as e:
        log(f"Erreur sauvegarde equalizer : {e}")
