import subprocess
from modules.bluetooth_config import BLUETOOTH_DEVICES

def list_bluetooth_devices():
    try:
        result = subprocess.check_output("bluetoothctl devices", shell=True).decode()
        devices = []
        for line in result.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                devices.append((parts[1], " ".join(parts[2:])))
        return devices
    except subprocess.CalledProcessError as e:
        print(f"[SPYNBOOX] Failed to list Bluetooth devices: {e}")
        return []

def connect_device(mac_address):
    try:
        subprocess.run(f"bluetoothctl connect {mac_address}", shell=True, check=True)
        print(f"[SPYNBOOX] Connected to {mac_address}")
    except subprocess.CalledProcessError:
        print(f"[SPYNBOOX] Failed to connect to {mac_address}")

def disconnect_device(mac_address):
    try:
        subprocess.run(f"bluetoothctl disconnect {mac_address}", shell=True, check=True)
        print(f"[SPYNBOOX] Disconnected from {mac_address}")
    except subprocess.CalledProcessError:
        print(f"[SPYNBOOX] Failed to disconnect {mac_address}")

def pair_device(mac_address):
    try:
        subprocess.run(f"bluetoothctl pair {mac_address}", shell=True, check=True)
        subprocess.run(f"bluetoothctl trust {mac_address}", shell=True, check=True)
        subprocess.run(f"bluetoothctl connect {mac_address}", shell=True, check=True)
        print(f"[SPYNBOOX] Paired and connected to {mac_address}")
    except subprocess.CalledProcessError:
        print(f"[SPYNBOOX] Failed to pair/connect to {mac_address}")

def is_output_connected(mac_address):
    """
    Vérifie si un périphérique Bluetooth est connecté à partir de son adresse MAC.
    Retourne True si connecté, False sinon.
    """
    try:
        result = subprocess.check_output(f"bluetoothctl info {mac_address}", shell=True).decode()
        return "Connected: yes" in result
    except Exception as e:
        print(f"[SPYNBOOX] Échec de vérification pour {mac_address} : {e}")
        return False
