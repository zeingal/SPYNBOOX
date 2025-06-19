
import sys
import traceback
import tkinter as tk
from tkinter import messagebox

from modules import interface
from modules.logger import setup_logger
from modules.config import load_global_config
from modules.rtc import init_rtc_module
from modules.battery import check_battery_status
from modules.update_checker import is_update_available, get_remote_version

import time

# Initialisation du système de log
logger = setup_logger()

def main():
    try:
        logger.info("[SPYNBOOX] Initialisation du système...")

        # Charger la configuration globale
        config = load_global_config()
        logger.info("Configuration chargée.")

        # Affichage des versions locale/distance
        local_version = config.get("version", "0.0.0")
        remote_version = get_remote_version()

        logger.info(f"[SPYNBOOX] Version locale détectée : {local_version}")
        if remote_version:
            logger.info(f"[SPYNBOOX] Version distante récupérée : {remote_version}")
            if remote_version != local_version:
                logger.warning("[SPYNBOOX] Une mise à jour est disponible !")
            else:
                logger.info("[SPYNBOOX] Aucune mise à jour disponible.")
        else:
            logger.warning("[SPYNBOOX] Impossible de récupérer la version distante.")

        # Initialiser le module RTC si présent
        init_rtc_module()

        # Vérifier l'état de la batterie
        check_battery_status()

        # Vérifier les mises à jour avec popup
        try:
            if is_update_available():
                logger.warning("[SPYNBOOX] Une mise à jour est disponible ! Consultez le dépôt.")
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Mise à jour disponible", "Une nouvelle version de SPYNBOOX est disponible.")
                root.destroy()
        except Exception as e:
            logger.warning(f"[SPYNBOOX] Impossible de vérifier les mises à jour : {e}")

        # Petit délai pour s’assurer que la fenêtre s'est bien fermée
        time.sleep(0.3)

        # Lancer l'interface principale
        interface.run_app()

    except Exception as e:
        logger.error("[SPYNBOOX] Une erreur critique est survenue :(")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
