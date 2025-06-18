try:
    from ina219 import INA219
    from ina219 import DeviceRangeError
    INA_AVAILABLE = True
except ImportError:
    INA_AVAILABLE = False
    print("[SPYNBOOX] INA219 non détecté : module 'battery.py' désactivé.")

SHUNT_OHMS = 0.1

def get_battery_level():
    """Retourne la tension de la batterie si le module est disponible."""
    if not INA_AVAILABLE:
        return None

    try:
        ina = INA219(SHUNT_OHMS)
        ina.configure()
        voltage = ina.voltage()
        return round(voltage, 2)
    except DeviceRangeError as e:
        print(f"[SPYNBOOX] Erreur INA219 : {e}")
        return None
    except Exception as e:
        print(f"[SPYNBOOX] Erreur inattendue : {e}")
        return None

def check_battery_status():
    """Fonction d'appel simple pour vérifier le niveau de batterie (ou désactivation)."""
    voltage = get_battery_level()
    if voltage is not None:
        print(f"[SPYNBOOX] Batterie : {voltage} V")
    else:
        print("[SPYNBOOX] INA219 non détecté ou erreur de lecture.")
