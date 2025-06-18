import logging
import os
from datetime import datetime

# === Création du dossier logs si nécessaire ===
LOG_DIR = "Logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# === Création du nom de fichier log basé sur la date ===
log_filename = datetime.now().strftime("spynboox_%Y-%m-%d.log")
log_path = os.path.join(LOG_DIR, log_filename)

# === Configuration du logger ===
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# === Fonctions pratiques pour les autres modules ===
def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_debug(message):
    logging.debug(message)

def setup_logger():
    # Permet un appel explicite si besoin
    log_info("Logger initialisé")

log = log_info

