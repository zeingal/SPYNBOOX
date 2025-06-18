# modules/config.py

import os
import json

CONFIG_FILE = os.path.expanduser("~/.spynboox_config.json")

DEFAULT_CONFIG = {
    "theme": "dark",
    "brightness": 70,
    "volume": 80,
    "equalizer": {
        "bass": 0,
        "medium": 0,
        "treble": 0
    },
    "bluetooth_outputs": {
        "output1": {"status": False, "mode": "stereo"},
        "output2": {"status": False, "mode": "stereo"},
        "output3": {"status": False, "mode": "stereo"}
    }
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return DEFAULT_CONFIG.copy()
    else:
        return DEFAULT_CONFIG.copy()

def save_config(config_data):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f, indent=4)
    except Exception as e:
        print(f"[SPYNBOOX] Failed to save config: {e}")

from modules.config import load_global_config
