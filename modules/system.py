import os
import subprocess

def shutdown_system():
    """Éteint proprement le Raspberry Pi."""
    try:
        print("[SPYNBOOX] Extinction en cours...")
        subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
    except Exception as e:
        print(f"[SPYNBOOX] Erreur lors de l'extinction : {e}")

def reboot_system():
    """Redémarre proprement le Raspberry Pi."""
    try:
        print("[SPYNBOOX] Redémarrage en cours...")
        subprocess.run(["sudo", "reboot"], check=True)
    except Exception as e:
        print(f"[SPYNBOOX] Erreur lors du redémarrage : {e}")
