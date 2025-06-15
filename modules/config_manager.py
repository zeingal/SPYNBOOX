# modules/config_manager.py

import os
import json

CONFIG_PATH = "/home/pi/SPYNBOOX/config"
CONFIG_FILE = os.path.join(CONFIG_PATH, "config.json")

DEFAULT_CONFIG = {
    "theme": "dark",
    "brightness": 80,
    "language": "fr",
    "volume_global": 70,
    "rtc_enabled": True,
    "battery_check": True,
    "audio_input": {
        "source": "Bluetooth (entrée)",
        "filepath": ""
    },
    "outputs": {
        "1": {"enabled": False, "mode": "ST"},
        "2": {"enabled": False, "mode": "ST"},
        "3": {"enabled": False, "mode": "ST"}
    }
}

# === Création du dossier config si nécessaire ===
def ensure_config_folder():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)

# === Chargement de la config ===
def load_config():
    ensure_config_folder()
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"[CONFIG] Error loading config: {e}")
        return DEFAULT_CONFIG

# === Sauvegarde de la config ===
def save_config(config):
    ensure_config_folder()
    try:
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        print("[CONFIG] Configuration saved.")
    except Exception as e:
        print(f"[CONFIG] Error saving config: {e}")

# === Mise à jour d'une valeur simple ===
def update_config_value(key, value):
    config = load_config()
    config[key] = value
    save_config(config)

def get_config_value(key, default=None):
    config = load_config()
    return config.get(key, default)

# === Gestion spécifique des sorties Bluetooth ===
def get_output_config(index):
    config = load_config()
    return config.get("outputs", {}).get(str(index), {"enabled": False, "mode": "ST"})

def set_output_mode(index, mode):
    config = load_config()
    outputs = config.setdefault("outputs", {})
    outputs[str(index)] = outputs.get(str(index), {})
    outputs[str(index)]["mode"] = mode
    save_config(config)

def set_output_status(index, enabled):
    config = load_config()
    outputs = config.setdefault("outputs", {})
    outputs[str(index)] = outputs.get(str(index), {})
    outputs[str(index)]["enabled"] = enabled
    save_config(config)

def get_output_mode(index):
    return get_output_config(index).get("mode", "ST")

def is_output_enabled(index):
    return get_output_config(index).get("enabled", False)
