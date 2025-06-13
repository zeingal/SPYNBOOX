 import sys
import traceback

from modules import interface
from modules.logging import setup_logger
from modules.config import load_global_config
from modules.rtc import init_rtc_module
from modules.battery import check_battery_status
from modules.update_checker import check_for_updates

logger = setup_logger()

def main():
    try:
        logger.info("[SPYNBOOX] Initialisation du système...")

        # Charger la configuration globale
        config = load_global_config()
        logger.info("Configuration chargée.")

        # Initialiser le module RTC si présent
        init_rtc_module()

        # Vérifier l'état de la batterie
        check_battery_status()

        # Vérifier les mises à jour
        check_for_updates()

        # Lancer l'interface principale
        interface.run_app()

    except Exception as e:
        logger.error("[SPYNBOOX] Une erreur critique est survenue :")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
