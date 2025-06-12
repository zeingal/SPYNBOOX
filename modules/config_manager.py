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
    "battery_check": True
}

def ensure_config_folder():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)

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

def save_config(config):
    ensure_config_folder()
    try:
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        print("[CONFIG] Configuration saved.")
    except Exception as e:
        print(f"[CONFIG] Error saving config: {e}")

def update_config_value(key, value):
    config = load_config()
    config[key] = value
    save_config(config)

def get_config_value(key, default=None):
    config = load_config()
    return config.get(key, default)
