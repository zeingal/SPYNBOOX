import modules.theme_manager as theme_manager
import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # Cadre principal
    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True, fill="both")

    # Titre SPYNBOOX
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=20)

    # Liste des boutons à afficher (page_name, texte, emoji)
    buttons = [
        ("audio", "Audio", "🎧"),
        ("equalizer", "Égaliseur", "🎚️"),
        ("bluetooth", "Bluetooth", "📡"),
        ("settings", "Paramètres", "⚙️"),
        ("shutdown", "Éteindre", "⏻")
    ]

    # Création des boutons avec espacement régulier
    for page_name, label, emoji in buttons:
        create_button(
            main_frame,
            text=f"{emoji} {label}",
            command=lambda p=page_name: navigate_callback(p),
            bg=COLORS["button"],
            fg=COLORS["button_text"],
            font=FONTS["button"]
        ).pack(pady=8)
