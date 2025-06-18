import datetime

try:
    import board
    import busio
    import adafruit_ds3231

    i2c = busio.I2C(board.SCL, board.SDA)
    rtc = adafruit_ds3231.DS3231(i2c)
    rtc_available = True

except Exception:
    rtc_available = False

def get_current_time():
    """Retourne l'heure actuelle depuis le module RTC ou le système si indisponible."""
    if rtc_available:
        try:
            return rtc.datetime
        except Exception:
            pass
    return datetime.datetime.now()

import subprocess
import datetime

def set_manual_time(hour, minute):
    """Définit l’heure manuellement sur le Raspberry Pi."""
    try:
        now = datetime.datetime.now()
        new_time = f"{hour:02d}:{minute:02d}:{now.day:02d}-{now.month:02d}-{now.year}"
        subprocess.run(["sudo", "date", "-s", new_time], check=True)
        print(f"[INFO] Heure définie manuellement : {new_time}")
    except Exception as e:
        print(f"[ERREUR] Impossible de définir l’heure manuelle : {e}")

def auto_sync_time():
    """Active la synchronisation automatique via NTP."""
    try:
        subprocess.run(["sudo", "timedatectl", "set-ntp", "true"], check=True)
        print("[INFO] Synchronisation NTP activée.")
    except Exception as e:
        print(f"[ERREUR] Impossible d’activer la synchronisation NTP : {e}")

def init_rtc_module():
    print("[SPYNBOOX] Module RTC initialisé")
