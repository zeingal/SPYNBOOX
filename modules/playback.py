import subprocess
import json
import os

# Dictionnaire pour stocker les processus de lecture en cours par sortie
playback_processes = {}

# Charger la config
def load_config():
    config_path = "config/config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {}

# Démarrer la lecture sur toutes les sorties configurées
def start_playback():
    stop_playback()  # Stopper d'abord les anciennes lectures
    config = load_config()

    source_config = config.get("audio_input", {})
    source_type = source_config.get("source", "Bluetooth (entrée)")
    filepath = source_config.get("filepath", "")

    # Choisir le flux audio selon la source
    if source_type == "Fichier local" and filepath:
        input_cmd = ["-i", filepath]
    else:
        # Exemple pour Bluetooth (entrée) – à adapter si flux audio réel
        input_cmd = ["-f", "pulse", "-i", "bluez_source"]

    for output_index in range(1, 4):
        mode = config.get("outputs", {}).get(str(output_index), {}).get("mode", "ST")
        output_device = f"bluealsa:DEV=XX:XX:XX:XX:XX:{output_index}"  # à adapter avec l’adresse réelle

        # Filtre audio selon le mode sélectionné
        if mode == "G":
            audio_filter = "pan=mono|c0=FL"
        elif mode == "D":
            audio_filter = "pan=mono|c0=FR"
        else:
            audio_filter = None  # stéréo

        # Commande ffmpeg
        cmd = ["ffmpeg"] + input_cmd
        if audio_filter:
            cmd += ["-af", audio_filter]
        cmd += ["-f", "wav", output_device]

        # Lancer le processus ffmpeg
        process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        playback_processes[output_index] = process

# Stopper toutes les lectures
def stop_playback():
    for process in playback_processes.values():
        if process and process.poll() is None:
            process.terminate()
    playback_processes.clear()

# Vérifier si une lecture est en cours
def is_playing():
    return any(proc.poll() is None for proc in playback_processes.values())
