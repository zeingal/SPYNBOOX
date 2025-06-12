# modules/audio_utils.py

import os
import wave
import contextlib

def audio_file_exists(file_path):
    """Vérifie si un fichier audio existe."""
    return os.path.isfile(file_path)

def get_audio_duration(file_path):
    """Retourne la durée d’un fichier WAV en secondes."""
    if not audio_file_exists(file_path):
        return 0.0
    try:
        with contextlib.closing(wave.open(file_path, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            return round(duration, 2)
    except Exception:
        return 0.0
