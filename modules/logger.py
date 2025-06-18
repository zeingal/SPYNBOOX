import logging
from datetime import datetime
import os

# === Dossier où stocker les logs ===
LOG_FOLDER = "logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# === Nom du fichier journal basé sur la date du jour ===
today = datetime.now().strftime("%Y-%m-%d")
log_filename = os.path.join(LOG_FOLDER, f"spynboox_{today}.log")

# === Fonction pour configurer le logger avec double sortie ===
def setup_logger():
    """Configure le logger pour SPYNBOOX avec double sortie (console + fichier)."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    logging.info("=== SPYNBOOX LANCÉ ===")

# === Fonctions de log pratiques ===
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
