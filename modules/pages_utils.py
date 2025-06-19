import tkinter as tk
from modules import theme_manager

# === Paramètres graphiques par défaut ===
FONT_DEFAULT = ("Bungee", 12)
COLOR_BUTTON = "#4CAF50"
COLOR_BUTTON_TEXT = "#FFFFFF"
COLOR_LABEL = "#333333"
COLOR_BACKGROUND = "#F0F0F0"
COLOR_SLIDER = "#FF6600"
SLIDER_LENGTH = 200
SLIDER_HEIGHT = 30  # Nouvelle hauteur visible

# === Bouton stylisé ===
def create_button(parent, text, command=None, width=15, bg=None, fg=None, font=None):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=font if font else FONT_DEFAULT,
        bg=bg if bg else theme_manager.COLORS.get("button", COLOR_BUTTON),
        fg=fg if fg else theme_manager.COLORS.get("button_text", COLOR_BUTTON_TEXT),
        activebackground="#cc5200",
        relief="raised",
        bd=2,
        width=width
    )

# === Label stylisé ===
def create_label(parent, text, font=FONT_DEFAULT, fg=None, bg=None):
    return tk.Label(
        parent,
        text=text,
        font=font,
        fg=fg if fg else theme_manager.COLORS.get("foreground", COLOR_LABEL),
        bg=bg if bg else theme_manager.COLORS.get("background", COLOR_BACKGROUND)
    )

# === Frame centrée ===
def create_frame(parent, padding=10, bg=None):
    return tk.Frame(
        parent,
        bg=bg if bg else theme_manager.COLORS.get("background", COLOR_BACKGROUND),
        padx=padding,
        pady=padding
    )

# === Bouton retour standard ===
def create_back_button(parent, command=None):
    return create_button(parent, "Retour", command=command, width=10)

# === Slider simple ===
def create_slider(parent, from_=0, to=100, command=None, orient=tk.HORIZONTAL):
    slider = tk.Scale(
        parent,
        from_=from_,
        to=to,
        orient=orient,
        length=SLIDER_LENGTH,
        fg=theme_manager.COLORS.get("foreground", COLOR_LABEL),
        bg=theme_manager.COLORS.get("background", COLOR_BACKGROUND),
        troughcolor="#DDDDDD",
        activebackground=theme_manager.COLORS.get("highlight", COLOR_SLIDER),
        font=FONT_DEFAULT,
        command=command,
        sliderlength=SLIDER_HEIGHT  # 🔧 Plus épais
    )
    return slider

# === Séparateur horizontal ===
def create_separator(parent):
    return tk.Frame(parent, height=2, bd=0, relief="flat", bg="#AAAAAA")
