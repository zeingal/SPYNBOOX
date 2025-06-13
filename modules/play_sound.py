# modules/play_sound.py

import os
import pygame
from modules.assets_manager import get_asset_path

# Initialiser Pygame Mixer une seule fois
pygame.mixer.init()

# Fonction pour jouer le son de notification (boom.wav)
def play_notification():
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
