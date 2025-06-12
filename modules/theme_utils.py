# modules/theme_utils.py

def get_theme_colors(theme):
    """Retourne un dictionnaire de couleurs en fonction du thème (jour ou nuit)."""
    if theme == "jour":
        return {
            "background": "#FFFFFF",
            "foreground": "#000000",
            "accent": "#FF6600",
            "button_bg": "#DDDDDD",
            "return_btn": "#6B8E23",  # vert olive
            "title": "#FF6600",
            "value": "#FF6600"
        }
    else:
        return {
            "background": "#2C2C2C",
            "foreground": "#FFFFFF",
            "accent": "#FF6600",
            "button_bg": "#444444",
            "return_btn": "#6B8E23",
            "title": "#FF6600",
            "value": "#FF6600"
        }

def get_font(theme):
    """Retourne le nom de la police à utiliser."""
    return ("Bungee", 14)

def get_slider_style(theme):
    """Retourne le style des sliders."""
    if theme == "jour":
        return {
            "trough_color": "#CCCCCC",
            "slider_color": "#FF6600"
        }
    else:
        return {
            "trough_color": "#555555",
            "slider_color": "#FF6600"
        }
