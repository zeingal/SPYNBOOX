import os
import subprocess

def shutdown_system():
    """
    Éteint proprement le système.
    """
    try:
        print("[POWER] Arrêt du système...")
        subprocess.run(['sudo', 'shutdown', '-h', 'now'], check=True)
    except Exception as e:
        print(f"[POWER] Erreur lors de l'arrêt : {e}")

def reboot_system():
    """
    Redémarre proprement le système.
    """
    try:
        print("[POWER] Redémarrage du système...")
        subprocess.run(['sudo', 'reboot'], check=True)
    except Exception as e:
        print(f"[POWER] Erreur lors du redémarrage : {e}")
