# modules/play_sound.py

import os
import pygame
import subprocess
from modules.assets_manager import get_asset_path
from modules.logging import log

# Initialiser le mixer Pygame une seule fois
pygame.mixer.init()

def play_notification():
    """
    Joue le son boom.wav pour les notifications globales
    """
    try:
        sound_path = get_asset_path("sounds", "boom.wav")
        if not os.path.exists(sound_path):
            print("[ERREUR] Le fichier boom.wav est introuvable.")
            return
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
        print("[INFO] Son de notification joué.")
    except Exception as e:
        print(f"[ERREUR] lors de la lecture de boom.wav : {e}")

def play_sound_file(sound_path: str, output_index: int):
    """
    Joue un son sur une sortie Bluetooth spécifique (test de sortie)
    """
    try:
        full_path = get_asset_path("sounds", sound_path)
        if not os.path.exists(full_path):
            log(f"[AUDIO] Fichier introuvable : {full_path}")
            return

        cmd = [
            "ffplay",
            "-nodisp", "-autoexit",
            "-volume", "100",
            full_path
        ]

        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log(f"[AUDIO] Test sonore lancé pour sortie {output_index}")
    except Exception as e:
        log(f"[AUDIO] Erreur lecture test sonore : {e}")
