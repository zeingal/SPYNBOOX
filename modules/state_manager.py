# modules/state_manager.py

import json
import os

STATE_FILE = "config.json"

DEFAULT_STATE = {
    "theme": "jour",
    "luminosity": 80,
    "volume_output_1": 50,
    "volume_output_2": 50,
    "volume_output_3": 50,
    "equalizer": {
        "bass": 0,
        "medium": 0,
        "treble": 0
    },
    "bluetooth_outputs": {
        "output_1": {"connected": False, "mode": "stereo"},
        "output_2": {"connected": False, "mode": "stereo"},
        "output_3": {"connected": False, "mode": "stereo"}
    },
    "last_mode": "main"
}

def load_state():
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE)
        return DEFAULT_STATE
    try:
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return DEFAULT_STATE

def save_state(state):
    try:
        with open(STATE_FILE, "w") as file:
            json.dump(state, file, indent=4)
    except Exception as e:
        print(f"[Erreur] Impossible de sauvegarder l'état : {e}")
