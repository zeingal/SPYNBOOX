import sys
import traceback
import tkinter as tk
from tkinter import messagebox

from modules import interface
from modules.logger import setup_logger, log_info, log_warning, log_error
from modules.config import load_global_config
from modules.rtc import init_rtc_module
from modules.battery import check_battery_status
from modules.update_checker import is_update_available

# Initialiser le système de log
setup_logger()

def main():
    try:
        log_info("[SPYNBOOX] Initialisation du système...")

        # Charger la configuration globale
        config = load_global_config()
        log_info("Configuration chargée.")

        # Initialiser le module RTC si présent
        init_rtc_module()

        # Vérifier l'état de la batterie
        check_battery_status()

        # Vérifier les mises à jour (console + popup)
        try:
            if is_update_available():
                log_warning("[SPYNBOOX] Une mise à jour est disponible ! Consultez les options.")

                # Affichage d'une alerte graphique
                root = tk.Tk()
                root.withdraw()  # Ne pas afficher de fenêtre principale
                messagebox.showinfo("Mise à jour disponible", "Une nouvelle version de SPYNBOOX est prête !")
                root.destroy()
            else:
                log_info("[SPYNBOOX] Aucune mise à jour disponible.")
        except Exception as e:
            log_warning(f"[SPYNBOOX] Impossible de vérifier les mises à jour : {e}")

        # Lancer l'interface principale
        interface.run_app()

    except Exception as e:
        log_error("[SPYNBOOX] Une erreur critique est survenue :")
        log_error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
