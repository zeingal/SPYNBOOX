# Configuration des périphériques Bluetooth

# Appareils déjà connus (nom : adresse MAC)
BLUETOOTH_DEVICES = {
    "Sortie1": "00:11:22:33:44:55",
    "Sortie2": "11:22:33:44:55:66",
    "Sortie3": "22:33:44:55:66:77"
}

# Nom générique à afficher si inconnu
DEFAULT_DEVICE_NAME = "Inconnu"

# Nom du périphérique source Bluetooth (smartphone, tablette)
BLUETOOTH_SOURCE_NAME = "Smartphone Seb"

# Mode par défaut : "stereo", "left", "right"
DEFAULT_OUTPUT_MODE = "stereo"

# Fichier de cache des connexions réussies (pour reconnexion auto)
PAIRED_DEVICES_FILE = "paired_devices.json"
