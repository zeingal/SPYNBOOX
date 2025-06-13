import tkinter as tk
from modules import (
    start_animation,
    theme_manager,
    display,
    pages_home,
    toast,
)
from modules.logger import setup_logger

logger = setup_logger()

def run_app():
    try:
        logger.info("[SPYNBOOX] Lancement de l'application")

        # Initialisation de la fenêtre principale
        root = tk.Tk()
        root.title("SPYNBOOX")
        root.geometry("480x320")
        root.configure(bg="black")
        root.attributes("-fullscreen", True)

        # Application du thème (jour/nuit)
        theme_manager.apply_theme(root)

        # Réglage initial de la luminosité
        display.set_brightness_from_config()

        # Fonction de démarrage après animation
        def launch_main_page():
            logger.info("[SPYNBOOX] Chargement de la page d'accueil")
            pages_home.display_home_page(root)

        # Animation de démarrage
        start_animation.play_start_animation(root, launch_main_page)

        # Lancement de l'application
        root.mainloop()

    except Exception as e:
        logger.error(f"[SPYNBOOX] Erreur critique dans l'application : {e}")
        toast.show_error_message(str(e))
