import sys
import traceback
import tkinter as tk
from tkinter import messagebox

from modules import interface
from modules.logger import setup_logger
from modules.config import load_global_config
from modules.rtc import init_rtc_module
from modules.battery import check_battery_status
from modules.update_checker import get_remote_version

logger = setup_logger()

def main():
    try:
        logger.info("[SPYNBOOX] Initialisation du système...")

        # Charger la configuration
        config = load_global_config()
        logger.info("Configuration chargée.")

        # Vérifier les versions
        local_version = config.get("version", "0.0.0")
        remote_version = get_remote_version()

        logger.info(f"[SPYNBOOX] Version locale : {local_version}")
        if remote_version:
            logger.info(f"[SPYNBOOX] Version distante : {remote_version}")
            if remote_version != local_version:
                logger.warning("[SPYNBOOX] Mise à jour disponible.")
                
                # Affichage de la fenêtre d'information
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Mise à jour disponible", "Une nouvelle version de SPYNBOOX est disponible.")
                root.destroy()
            else:
                logger.info("[SPYNBOOX] Pas de mise à jour nécessaire.")
        else:
            logger.warning("[SPYNBOOX] Version distante inaccessible.")

        # Initialisations techniques
        init_rtc_module()
        check_battery_status()

        # Lancer SPYNBOOX
        logger.info("[SPYNBOOX] Lancement de l'application principale")
        interface.run_app()

    except Exception as e:
        logger.error("[SPYNBOOX] Erreur critique :")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
