# modules/playback.py

import subprocess
import os
import signal

from modules.audio_input import get_audio_input_command
from modules.config_manager import load_config

playback_process = None  # process global pour arrêt facile

def start_playback():
    global playback_process

    # Si une lecture est déjà en cours, on la stoppe
    if playback_process and playback_process.poll() is None:
        stop_playback()

    # Obtenir la source sélectionnée
    source_info = get_audio_input_command()
    if source_info["type"] == "error":
        print("Erreur source audio :", source_info["message"])
        return
    elif source_info["type"] == "unsupported":
        print("Source non prise en charge :", source_info["message"])
        return

    # Obtenir config des sorties BT
    config = load_config()
    sorties = config.get("bluetooth_outputs", {})
    active_outputs = [key for key, val in sorties.items() if val.get("enabled")]

    if not active_outputs:
        print("Aucune sortie Bluetooth active.")
        return

    # Commande de base selon type
    if source_info["type"] == "file":
        filepath = source_info["filepath"]
        # Lecture avec ffmpeg et redirection vers bluealsa ou autre
        command = [
            "ffmpeg", "-re", "-i", filepath,
            "-f", "wav", "-"
        ]
    elif source_info["type"] == "stream":
        # Commande arecord ou autre
        command = source_info["command"].split()

    # Exemple : redirection via pipe à venir
    # Pour le moment : test avec simple lecture stdout
    print("Démarrage lecture :", " ".join(command))

    try:
        playback_process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print("Erreur lancement playback :", e)

def stop_playback():
    global playback_process
    if playback_process and playback_process.poll() is None:
        playback_process.terminate()
        try:
            playback_process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            playback_process.kill()
    playback_process = None

def is_playing():
    global playback_process
    return playback_process is not None and playback_process.poll() is None
