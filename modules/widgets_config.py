# widgets_config.py

# Configuration graphique des widgets de l'interface

COLORS = {
    "background_day": "#FFFFFF",
    "background_night": "#3C3F41",
    "foreground": "#000000",
    "highlight": "#FF6600",
    "button_bg": "#CCCCCC",
    "button_fg": "#000000",
    "slider_trough": "#EEEEEE",
    "slider_thumb": "#FF6600",
    "green_olive": "#708238",

    # Clés critiques pour pages_audio.py
    "background": "black",
    "accent": "#00FFFF",
    "button": "green",
    "button_text": "white",
    "return": "#333333",
    "green": "green",
    "red": "red"
}

# Polices
FONTS = {
    "title": ("Bungee", 20),
    "label": ("Arial", 12),
    "button": ("Arial", 11, "bold"),
    "slider": ("Arial", 10)
}

# Dimensions standards
DIMENSIONS = {
    "button_width": 12,
    "slider_length": 180,
    "padding": 8
}

# Alias rétrocompatibles
FONT_TITRE = FONTS["title"]
FONT_STANDARD = FONTS["label"]
COULEUR_FOND = COLORS["background_day"]
COULEUR_BOUTON = COLORS["highlight"]
COULEUR_TEXTE = COLORS["foreground"]
