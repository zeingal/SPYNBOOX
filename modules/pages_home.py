import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def create_home_page(root, navigate_callback):
    # Efface les widgets précédents
    for widget in root.winfo_children():
        widget.destroy()

    # Cadre principal centré
    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True)

    # Titre
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=20)

    # Boutons de navigation
    buttons_info = [
        ("🔊 Audio", lambda: navigate_callback("audio")),
        ("🎚️ Égaliseur", lambda: navigate_callback("equalizer")),
        ("📡 Bluetooth", lambda: navigate_callback("bluetooth")),
        ("⚙️ Paramètres", lambda: navigate_callback("settings")),
        ("⏻ Éteindre", lambda: navigate_callback("shutdown"))
    ]

    for text, command in buttons_info:
        create_button(
            main_frame,
            text=text,
            command=command,
            bg=COLORS["button"],
            fg=COLORS["button_text"],
            font=FONTS["button"]
        ).pack(pady=10, ipadx=10, ipady=5)
