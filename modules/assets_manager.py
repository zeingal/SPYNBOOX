# modules/assets_manager.py

import os

ASSETS_BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "Assets")

def get_asset_path(relative_path):
    """
    Renvoie le chemin absolu d'un fichier dans le dossier Assets
    Exemple : get_asset_path("sounds/boom.wav")
    """
    return os.path.abspath(os.path.join(ASSETS_BASE_PATH, relative_path))
