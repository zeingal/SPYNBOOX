import tkinter as tk
import json
import os

from modules.widgets_config import COLORS, FONTS
from modules.pages_utils import create_frame, create_label, create_button
from modules.config_manager import load_config, save_config

def create_mode_selection_page(root, navigate_callback, output_index):
    for widget in root.winfo_children():
        widget.destroy()

    frame = create_frame(root)
    frame.pack(expand=True, fill="both")

    # Titre
    create_label(
        frame,
        text=f"🔊 Sortie {output_index} – Mode audio",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=10)

    # Récupérer le mode actuel
    config = load_config()
    current_mode = config.get("outputs", {}).get(str(output_index), {}).get("mode", "ST")

    # Fonction de sauvegarde
    def set_mode(mode):
        if "outputs" not in config:
            config["outputs"] = {}
        if str(output_index) not in config["outputs"]:
            config["outputs"][str(output_index)] = {}

        config["outputs"][str(output_index)]["mode"] = mode
        save_config(config)
        navigate_callback("audio")  # Retour à la page audio

    # Boutons de sélection
    btn_frame = create_frame(frame)
    btn_frame.pack(pady=10)

    for mode, label in [("ST", "Stéréo"), ("G", "Gauche"), ("D", "Droite")]:
        color = COLORS["accent"] if mode == current_mode else COLORS["button"]
        create_button(
            btn_frame,
            text=label,
            command=lambda m=mode: set_mode(m),
            bg=color,
            fg=COLORS["button_text"],
            font=FONTS["button"],
            width=10
        ).pack(pady=5)

    # Bouton retour sans changement
    create_button(
        frame,
        text="Retour",
        command=lambda: navigate_callback("audio"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=15)
