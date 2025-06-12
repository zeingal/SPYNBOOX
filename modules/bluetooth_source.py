import subprocess
import time

def make_discoverable():
    try:
        subprocess.run(["bluetoothctl", "discoverable", "on"], check=True)
        subprocess.run(["bluetoothctl", "pairable", "on"], check=True)
        subprocess.run(["bluetoothctl", "agent", "on"], check=True)
        subprocess.run(["bluetoothctl", "default-agent"], check=True)
        print("[SPYNBOOX] Appairage source activé")
    except subprocess.CalledProcessError as e:
        print(f"[SPYNBOOX] Erreur activation appairage source : {e}")

def is_connected():
    try:
        result = subprocess.run(
            ["bluetoothctl", "info"],
            capture_output=True,
            text=True
        )
        return "Connected: yes" in result.stdout
    except Exception as e:
        print(f"[SPYNBOOX] Erreur vérification connexion source : {e}")
        return False
