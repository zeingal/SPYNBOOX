import os
import pygame

# Initialiser le mixer Pygame une seule fois
pygame.mixer.init()

# Répertoire des sons
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "sounds")

# Dictionnaire des sons
SOUNDS = {
    "click": "click.wav",
    "confirm": "confirm.wav",
    "error": "error.wav",
    "startup": "startup.wav"
}

def play_sound(name):
    """Joue un effet sonore par nom (s'il existe)."""
    filename = SOUNDS.get(name)
    if not filename:
        print(f"[SoundFX] Son '{name}' introuvable dans le dictionnaire.")
        return

    path = os.path.join(SOUND_DIR, filename)

    if not os.path.isfile(path):
        print(f"[SoundFX] Fichier son manquant : {path}")
        return

    try:
        sound = pygame.mixer.Sound(path)
        sound.play()
    except Exception as e:
        print(f"[SoundFX] Erreur lors de la lecture du son '{name}' : {e}")
