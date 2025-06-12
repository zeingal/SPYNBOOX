# modules/wifi_utils.py

import subprocess
import re

def get_wifi_ssid():
    """Retourne le nom du réseau Wi-Fi (SSID) connecté"""
    try:
        output = subprocess.check_output(["iwgetid", "--raw"]).decode().strip()
        return output if output else "Non connecté"
    except Exception as e:
        print(f"Erreur récupération SSID : {e}")
        return "Erreur"

def get_ip_address():
    """Retourne l'adresse IP locale"""
    try:
        output = subprocess.check_output(["hostname", "-I"]).decode().strip()
        return output.split()[0] if output else "Non attribuée"
    except Exception as e:
        print(f"Erreur récupération IP : {e}")
        return "Erreur"
