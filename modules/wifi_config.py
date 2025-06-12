# modules/wifi_config.py

import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

def load_wifi_config():
    """Charge les paramètres Wi-Fi depuis le fichier config.json."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config.get("wifi", {})
    except Exception as e:
        print(f"Erreur de chargement du Wi-Fi : {e}")
        return {}

def save_wifi_config(ssid, password):
    """Sauvegarde les paramètres Wi-Fi dans le fichier config.json."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)

        config["wifi"] = {
            "ssid": ssid,
            "password": password
        }

        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Erreur de sauvegarde du Wi-Fi : {e}")
        return False
