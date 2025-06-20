from modules import (
    pages_home,
    pages_audio,
    pages_equalizer,
    pages_bluetooth,
    pages_settings,
    shutdown
)

def navigate_to(page_name, root,
                apply_theme_callback=None,
                set_brightness_callback=None,
                set_manual_time=None,
                auto_sync_time=None,
                update_system=None,
                shutdown_device=None):

    page_name = page_name.lower()
    print(f"[DEBUG] Navigation vers : {page_name}")

    if page_name == "home":
        print("[DEBUG] Appel page_home")
        pages_home.display_home_page(root, navigate_to)

    elif page_name == "audio":
        print("[DEBUG] Appel page_audio")
        pages_audio.create_audio_page(root, navigate_to)

    elif page_name == "equalizer":
        print("[DEBUG] Appel page_equalizer")
        pages_equalizer.create_equalizer_page(root, navigate_to)

    elif page_name == "bluetooth":
        print("[DEBUG] Appel page_bluetooth")
        pages_bluetooth.create_bluetooth_page(root, navigate_to)

    elif page_name == "settings":
        print("[DEBUG] Appel page_settings")
        pages_settings.create_settings_page(
            root,
            navigate_to,
            apply_theme_callback,
            set_brightness_callback,
            set_manual_time,
            auto_sync_time,
            update_system,
            shutdown_device
        )

    elif page_name == "shutdown":
        print("[DEBUG] Appel shutdown")
        shutdown.shutdown_device()

    else:
        print(f"[SPYNBOOX] Erreur : Page inconnue '{page_name}'")
