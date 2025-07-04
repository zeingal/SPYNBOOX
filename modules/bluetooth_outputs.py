import subprocess

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
        print(f"[SPYNBOOX] Failed to disconnect from {mac_address}")

def pair_device(mac_address):
    try:
        subprocess.run(f"bluetoothctl pair {mac_address}", shell=True, check=True)
        subprocess.run(f"bluetoothctl trust {mac_address}", shell=True, check=True)
        subprocess.run(f"bluetoothctl connect {mac_address}", shell=True, check=True)
        print(f"[SPYNBOOX] Paired and connected to {mac_address}")
    except subprocess.CalledProcessError:
        print(f"[SPYNBOOX] Failed to pair/connect to {mac_address}")

def is_output_connected(mac_address):
    try:
        result = subprocess.check_output("bluetoothctl info", shell=True).decode()
        return f"Device {mac_address}" in result and "Connected: yes" in result
    except subprocess.CalledProcessError:
        return False

def pair_device_to_output(mac_address):
    pair_device(mac_address)


import subprocess
import time

def list_nearby_devices(timeout=8):
    """
    Scanne les périphériques Bluetooth à proximité.
    Retourne une liste de tuples (adresse, nom).
    """
    try:
        subprocess.run(["bluetoothctl", "scan", "on"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(timeout)
        output = subprocess.check_output(["bluetoothctl", "devices"]).decode()
        subprocess.run(["bluetoothctl", "scan", "off"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        devices = []
        for line in output.splitlines():
            parts = line.strip().split(" ", 2)
            if len(parts) == 3:
                _, address, name = parts
                devices.append((address, name))
        return devices

    except Exception as e:
        print(f"[ERREUR] Scan Bluetooth échoué : {e}")
        return []
