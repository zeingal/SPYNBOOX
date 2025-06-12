import datetime
import os

LOG_FILE = os.path.expanduser("~/SPYNBOOX.log")

def log_event(message: str):
    """Ajoute un événement au fichier log avec horodatage."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

def log_error(error: Exception):
    """Enregistre une erreur dans le fichier log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_entry = f"[{timestamp}] [ERROR] {type(error).__name__}: {error}\n"
    with open(LOG_FILE, "a") as file:
        file.write(error_entry)
