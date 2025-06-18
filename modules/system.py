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

def update_system():
    """Lance une mise à jour système via apt-get."""
    try:
        print("[SPYNBOOX] Mise à jour système en cours...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        print("[SPYNBOOX] Mise à jour terminée.")
    except Exception as e:
        print(f"[SPYNBOOX] Erreur lors de la mise à jour : {e}")

def shutdown_device():
    """Alias de shutdown pour cohérence avec le reste de l’interface."""
    shutdown_system()
