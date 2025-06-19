def run_app():
    try:
        logger.info("[SPYNBOOX] Lancement de l'application")

        # Initialisation de la fenêtre principale
        root = tk.Tk()
        logger.info("[SPYNBOOX] Fenêtre principale créée")
        root.title("SPYNBOOX")
        root.geometry("480x320")
        root.configure(bg="black")
        root.attributes("-fullscreen", True)

        # Application du thème
        logger.info("[SPYNBOOX] Application du thème...")
        theme_manager.apply_theme(root)

        # Luminosité initiale
        logger.info("[SPYNBOOX] Réglage de la luminosité...")
        display.set_brightness_from_config()

        # Lancement après animation
        def launch_main_page():
            logger.info("[SPYNBOOX] Chargement de la page d'accueil")
            pages_home.display_home_page(root, navigate_callback)

        # Navigation avec hooks
        def navigate_callback(page_name):
            logger.info(f"[SPYNBOOX] Navigation vers : {page_name}")
            navigator.navigate_to(
                page_name,
                root,
                apply_theme_callback=theme_manager.apply_theme,
                set_brightness_callback=display.set_brightness,
                set_manual_time=rtc.set_manual_time,
                auto_sync_time=rtc.auto_sync_time,
                update_system=system.update_system,
                shutdown_device=system.shutdown_device
            )

        # Animation + lancement
        logger.info("[SPYNBOOX] Lancement direct de la page d'accueil sans animation")
        launch_main_page()

        logger.info("[SPYNBOOX] Démarrage de la boucle principale Tkinter")
        root.mainloop()

    except Exception as e:
        logger.error(f"[SPYNBOOX] Erreur critique dans l'application : {e}")
        toast.show_error_message(str(e))
