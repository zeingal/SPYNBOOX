# modules/update_checker.py

import json
import urllib.request
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
REMOTE_VERSION_URL = "https://raw.githubusercontent.com/zeingal/SPYNBOOX/main/version.txt"

def get_local_version():
    """Récupère la version locale depuis config.json"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config.get("version", "0.0.0")
    except Exception as e:
        print(f"Erreur de lecture de la version locale : {e}")
        return "0.0.0"

def get_remote_version():
    """Récupère la version distante depuis GitHub"""
    try:
        with urllib.request.urlopen(REMOTE_VERSION_URL) as response:
            return response.read().decode().strip()
    except Exception as e:
        print(f"Erreur de récupération de la version distante : {e}")
        return None

def is_update_available():
    """Compare les versions locale et distante"""
    local = get_local_version()
    remote = get_remote_version()
    if not remote:
        return False
    return remote != local
