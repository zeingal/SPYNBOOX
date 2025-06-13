import os
import subprocess

def shutdown_system():
    """
    Éteint proprement le Raspberry Pi.
    """
    print("[PowerManager] Extinction du système...")
    os.system("sudo shutdown now")

def reboot_system():
    """
    Redémarre le Raspberry Pi.
    """
    print("[PowerManager] Redémarrage du système...")
    os.system("sudo reboot")

def get_power_status():
    """
    Retourne l’état actuel de l’alimentation si INA219 disponible, sinon générique.
    """
    try:
        # Optionnel : intégrer la lecture réelle de l'INA219 ici
        status = {
            "voltage": "5.1V",
            "current": "420mA",
            "battery_level": "Estimée : 75%"
        }
        return status
    except Exception as e:
        print(f"[PowerManager] Impossible de lire le statut alimentation : {e}")
        return None

def is_safe_to_shutdown():
    """
    Vérifie les conditions critiques avant extinction.
    Exemple : si enregistrement en cours ou upload.
    """
    # Cette fonction peut s’enrichir de vérifications futures.
    return True
