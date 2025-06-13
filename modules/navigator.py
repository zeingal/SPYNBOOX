# navigator.py
from modules import (
    pages_home,
    pages_audio,
    pages_equalizer,
    pages_bluetooth,
    pages_settings,
    shutdown
)

def navigate_to(page_name, root):
    """
    Redirige vers la page spécifiée par son nom.
    """
    page_name = page_name.lower()
    
    if page_name == "home":
        pages_home.display_home_page(root)
    elif page_name == "audio":
        pages_audio.create_audio_page(root, navigate_to)
    elif page_name == "equalizer":
        pages_equalizer.create_equalizer_page(root, navigate_to)
    elif page_name == "bluetooth":
        pages_bluetooth.create_bluetooth_page(root, navigate_to)
    elif page_name == "settings":
        pages_settings.create_settings_page(root, navigate_to,
                                            apply_theme_callback=None,
                                            set_brightness_callback=None,
                                            set_manual_time=None,
                                            auto_sync_time=None,
                                            update_system=None,
                                            shutdown_device=None)
    elif page_name == "shutdown":
        shutdown.shutdown_device()
    else:
        print(f"[SPYNBOOX] Erreur : Page inconnue '{page_name}'")
