import os
import subprocess
import time

def shutdown_device():
    """
    Effectue une extinction propre du système.
    Peut être appelé par un bouton physique ou depuis l'interface logicielle.
    """
    try:
        print("[SPYNBOOX] Extinction du système en cours...")
        time.sleep(1)
        subprocess.run(['sudo', 'shutdown', '-h', 'now'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[SPYNBOOX] Échec de l'extinction : {e}")
    except Exception as e:
        print(f"[SPYNBOOX] Erreur inattendue pendant l'extinction : {e}")

def restart_device():
    """
    Redémarre le système proprement.
    """
    try:
        print("[SPYNBOOX] Redémarrage du système...")
        time.sleep(1)
        subprocess.run(['sudo', 'reboot'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[SPYNBOOX] Échec du redémarrage : {e}")
    except Exception as e:
        print(f"[SPYNBOOX] Erreur inattendue pendant le redémarrage : {e}")
