import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # === Sécurisation des couleurs ===
    background = COLORS.get("background", "#FFFFFF")  # blanc par défaut
    accent = COLORS.get("accent", "#000000")          # noir par défaut
    button_bg = COLORS.get("button", "#4CAF50")       # vert
    button_fg = COLORS.get("button_text", "#FFFFFF")  # blanc
    return_bg = COLORS.get("return", "#888888")       # gris

    # Cadre principal
    main_frame = create_frame(root, bg=background)
    main_frame.pack(expand=True, fill="both")

    # Titre SPYNBOOX
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS["title"],
        fg=accent,
        bg=background
    ).pack(pady=20)

    # Liste des boutons (page_name, texte, emoji)
    buttons = [
        ("audio", "Audio", "🎧"),
        ("equalizer", "Égaliseur", "🎚️"),
        ("bluetooth", "Bluetooth", "📡"),
        ("settings", "Paramètres", "⚙️"),
        ("shutdown", "Éteindre", "⏻")
    ]

    # Création des boutons
    for page_name, label, emoji in buttons:
        create_button(
            main_frame,
            text=f"{emoji} {label}",
            command=lambda p=page_name: navigate_callback(p),
            bg=button_bg,
            fg=button_fg,
            font=FONTS["button"]
        ).pack(pady=10)
