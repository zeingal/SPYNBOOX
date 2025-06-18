import logging
from datetime import datetime
import os

# Dossier des logs
LOG_FOLDER = "logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# Nom du fichier journal par date
today = datetime.now().strftime("%Y-%m-%d")
log_filename = os.path.join(LOG_FOLDER, f"spynboox_{today}.log")

# === Fonctions de log ===

def log_info(message):
    print(f"[INFO] {message}")
    logging.info(message)

def log_warning(message):
    print(f"[WARN] {message}")
    logging.warning(message)

def log_error(message):
    print(f"[ERROR] {message}")
    logging.error(message)

def log_debug(message):
    print(f"[DEBUG] {message}")
    logging.debug(message)

# === Setup logger (version propre sans conflit handlers/filename) ===

def setup_logger():
    """Initialise le logger avec sortie fichier + console."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Nettoyer les anciens handlers s’ils existent
    if logger.hasHandlers():
        logger.handlers.clear()

    # Handler fichier
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("=== SPYNBOOX LANCÉ ===")
