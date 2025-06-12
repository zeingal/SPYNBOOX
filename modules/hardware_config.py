# Configuration matérielle centralisée

# GPIO des LED RGB (version évoluée)
LED_R_PIN = 17
LED_G_PIN = 27
LED_B_PIN = 22

# GPIO du ventilateur
FAN_PIN = 23
TEMP_THRESHOLD = 50  # °C – seuil de température pour activer le ventilateur

# GPIO pour bouton physique de réveil écran ou extinction
BUTTON_WAKE_PIN = 24
BUTTON_SHUTDOWN_PIN = 25

# Durée avant mise en veille de l'écran après démarrage de l'enregistrement
SCREEN_SLEEP_DELAY = 10  # secondes

# Fréquence de mesure de température
TEMP_CHECK_INTERVAL = 5  # secondes

# Fichier de configuration du système (luminosité, thème, etc.)
CONFIG_FILE = "config.json"

# Paramètres du RTC
RTC_I2C_ADDRESS = 0x68  # pour DS3231

# Dossier par défaut pour les médias
MEDIA_FOLDER = "/home/pi/Videos/"

# Titre par défaut en cas de saisie vide
DEFAULT_VIDEO_TITLE = "captora_video"

# Position de l’horloge à l’écran
CLOCK_POSITION = "top_right"

# Position de l’icône batterie
BATTERY_POSITION = "top_right"
