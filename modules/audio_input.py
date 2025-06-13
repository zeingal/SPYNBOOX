# modules/audio_input.py

import os
from modules.config_manager import load_config

def get_audio_input_source():
    """Retourne le nom de la source sélectionnée depuis config.json"""
    config = load_config()
    audio_input = config.get("audio_input", {})
    return audio_input.get("source", None), audio_input

def get_audio_input_command():
    """
    Retourne la commande ou le paramètre à utiliser pour démarrer la lecture/capture
    en fonction de la source sélectionnée.
    """
    source, details = get_audio_input_source()

    if source == "Bluetooth (entrée)":
        # Exemple de lecture via bluealsa ou pulseaudio
        # À adapter selon la stack installée
        return {
            "type": "stream",
            "command": "arecord -D bluealsa -f cd"
        }

    elif source == "Fichier local":
        filepath = details.get("filepath")
        if not filepath or not os.path.isfile(filepath):
            return {
                "type": "error",
                "message": "Fichier audio introuvable. Merci d’en choisir un autre."
            }
        return {
            "type": "file",
            "filepath": filepath
        }

    elif source == "Jack 3,5 mm":
        return {
            "type": "unsupported",
            "message": "Entrée Jack non disponible dans cette version."
        }

    elif source == "RCA stéréo":
        return {
            "type": "unsupported",
            "message": "Entrée RCA non disponible dans cette version."
        }

    elif source == "HDMI audio":
        return {
            "type": "unsupported",
            "message": "Entrée HDMI non disponible dans cette version."
        }

    return {
        "type": "error",
        "message": "Aucune source audio valide sélectionnée."
    }

def is_audio_input_valid():
    """Retourne True si la source actuelle est utilisable"""
    result = get_audio_input_command()
    return result.get("type") in ("file", "stream")
