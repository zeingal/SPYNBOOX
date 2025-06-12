# modules/bluetooth_utils.py

import subprocess

def scan_devices():
    try:
        output = subprocess.check_output("bluetoothctl scan on", shell=True, timeout=10)
        return output.decode()
    except Exception as e:
        return f"Erreur scan : {e}"

def list_paired_devices():
    try:
        output = subprocess.check_output("bluetoothctl paired-devices", shell=True)
        return output.decode()
    except Exception as e:
        return f"Erreur paired-devices : {e}"

def connect_device(mac_address):
    try:
        output = subprocess.check_output(f"bluetoothctl connect {mac_address}", shell=True, timeout=5)
        return output.decode()
    except Exception as e:
        return f"Erreur connexion : {e}"

def disconnect_device(mac_address):
    try:
        output = subprocess.check_output(f"bluetoothctl disconnect {mac_address}", shell=True)
        return output.decode()
    except Exception as e:
        return f"Erreur déconnexion : {e}"
