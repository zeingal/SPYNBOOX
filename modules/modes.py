# modules/modes.py

import tkinter as tk
from modules.pages_utils import create_label, create_button, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.config_manager import load_config, save_config

def create_mode_selection_page(root, navigate_callback, output_index):
    config = load_config()
    output_key = f"output{output_index}"

    # Efface les widgets précédents
    for widget in root.winfo_children():
        widget.destroy()

    # Cadre principal
    frame = create_frame(root, bg=COLORS["background"])
    frame.pack(expand=True, fill="both")

    create_label(
        frame,
        text=f"🎚️ Mode de sortie {output_index}",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=10)

    # Options disponibles
    MODES = {
        "stereo": "🔊 Stéréo",
        "left": "🔈 Gauche",
        "right": "🔈 Droite"
    }

    def select_mode(mode):
        config["bluetooth_outputs"][output_key]["mode"] = mode
        save_config(config)
        navigate_callback("audio")  # Revenir à la page audio

    # Crée un bouton pour chaque mode
    for mode_key, mode_label in MODES.items():
        create_button(
            frame,
            text=mode_label,
            command=lambda m=mode_key: select_mode(m),
            bg=COLORS["button"],
            fg=COLORS["button_text"],
            font=FONTS["button"]
        ).pack(pady=5)

    # Bouton retour
    create_button(
        frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("audio"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=15)
