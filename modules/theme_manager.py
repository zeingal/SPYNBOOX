from modules import config, logger

# Thèmes possibles : jour / nuit
THEMES = {
    "day": {
        "background": "#FFFFFF",
        "foreground": "#000000",
        "button_color": "#4CAF50",  # Vert olive
        "highlight": "#FF6600",     # Orange
    },
    "night": {
        "background": "#556B2F",    # Vert olive foncé
        "foreground": "#FFFFFF",
        "button_color": "#FF6600",
        "highlight": "#FFD700",     # Or
    }
}

def get_current_theme():
    try:
        cfg = config.load_config()
        theme_name = cfg.get("theme", "day")
        return THEMES.get(theme_name, THEMES["day"])
    except Exception as e:
        logger.log_error(f"Erreur récupération thème : {e}")
        return THEMES["day"]

def apply_theme(widget, theme_data):
    global COLORS
    COLORS = theme_data  # stocke les couleurs en global
    try:
        widget.configure(bg=theme_data["background"])
        for child in widget.winfo_children():
            try:
                child.configure(
                    bg=theme_data["background"],
                    fg=theme_data["foreground"]
                )
            except:
                pass
    except Exception as e:
        logger.log_error(f"Erreur application thème : {e}")

def set_theme(theme_name):
    try:
        if theme_name in THEMES:
            cfg = config.load_config()
            cfg["theme"] = theme_name
            config.save_config(cfg)
            logger.log_info(f"Thème défini : {theme_name}")
    except Exception as e:
        logger.log_error(f"Erreur changement de thème : {e}")
