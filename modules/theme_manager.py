from modules import config, logger

# === Thèmes possibles : jour / nuit ===
THEMES = {
    "day": {
        "background": "#FFFFFF",       # Blanc
        "foreground": "#000000",       # Noir
        "button":     "#4CAF50",       # Vert olive
        "button_text": "#FFFFFF",      # Texte blanc
        "highlight":  "#FF6600",       # Orange
        "accent":     "#0066CC"        # Bleu
    },
    "night": {
        "background": "#556B2F",       # Vert olive foncé
        "foreground": "#FFFFFF",       # Blanc
        "button":     "#FF6600",       # Orange
        "button_text": "#000000",      # Texte noir
        "highlight":  "#FFD700",       # Or
        "accent":     "#3399FF"        # Bleu clair
    }
}

# === Donne le thème actuel depuis config.json ===
def get_current_theme():
    try:
        cfg = config.load_config()
        theme_name = cfg.get("theme", "day")
        return THEMES.get(theme_name, THEMES["day"])
    except Exception as e:
        logger.log_error(f"[Erreur] Chargement du thème échoué : {e}")
        return THEMES["day"]

# === Applique le thème aux widgets (et stocke globalement) ===
def apply_theme(widget, theme_data):
    global COLORS
    COLORS = theme_data  # Stockage global

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

# === Enregistre un nouveau thème choisi ===
def set_theme(theme_name):
    try:
        if theme_name in THEMES:
            cfg = config.load_config()
            cfg["theme"] = theme_name
            config.save_config(cfg)
            logger.log_info(f"Thème défini : {theme_name}")
    except Exception as e:
        logger.log_error(f"Erreur changement de thème : {e}")
