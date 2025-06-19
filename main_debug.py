
from tkinter import Tk
from modules.pages_home import display_home_page
from modules.theme_manager import apply_theme, get_current_theme
from modules.navigator import navigate_to
import logging

# Configuration du logger de debug
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("SPYNBOOX_DEBUG")

def run_debug():
    logger.debug("[DEBUG] Lancement de SPYNBOOX en mode debug")

    root = Tk()
    root.title("SPYNBOOX DEBUG")
    root.geometry("480x320")
    root.configure(bg="black")

    # Initialisation du thème
    logger.debug("[DEBUG] Application du thème (mode debug)")
    theme_data = get_current_theme()
    apply_theme(root, theme_data)

    # Navigation callback simplifié
    def navigate_callback(page_name):
        logger.debug(f"[DEBUG] Navigation vers : {page_name}")
        navigate_to(page_name, root)

    # Lancement de la page principale
    logger.debug("[DEBUG] Affichage de la page d'accueil")
    display_home_page(root, navigate_callback)

    # Boucle principale Tkinter
    logger.debug("[DEBUG] Boucle Tkinter démarrée")
    root.mainloop()

if __name__ == "__main__":
    run_debug()
