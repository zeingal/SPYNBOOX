# modules/sound.py

import os
import pygame

pygame.mixer.init()

def play_system_sound(filename):
    """
    Joue un son système (WAV, MP3...) depuis le dossier 'sounds'
    """
    try:
        sound_path = os.path.join('sounds', filename)
        if os.path.exists(sound_path):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            return True
        else:
            print(f"[SOUND] Fichier introuvable : {filename}")
            return False
    except Exception as e:
        print(f"[SOUND] Erreur lecture son : {e}")
        return False
