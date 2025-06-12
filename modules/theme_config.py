# Définition des thèmes et paramètres liés

theme_colors = {
    "day": {
        "bg": "#FFFFFF",
        "fg": "#000000",
        "button": "#FF6600",
        "button_text": "#FFFFFF",
        "accent": "#006400",
    },
    "night": {
        "bg": "#003300",
        "fg": "#FFFFFF",
        "button": "#FF6600",
        "button_text": "#FFFFFF",
        "accent": "#00FF00",
    }
}

def get_theme_colors(mode):
    """
    Retourne les couleurs associées au thème spécifié : 'day' ou 'night'
    """
    return theme_colors.get(mode, theme_colors["day"])
