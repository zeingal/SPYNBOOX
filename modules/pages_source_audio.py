# modules/pages_source_audio.py

import tkinter as tk
from tkinter import filedialog
import json
import os

from modules.widgets_config import FONT_TITRE, FONT_STANDARD, COULEUR_FOND, COULEUR_BOUTON, COULEUR_TEXTE
from modules.pages_utils import create_title_label, create_button, create_separator, create_status_label
from modules.config_manager import load_config, save_config

AUDIO_SOURCES = [
    {"name": "Bluetooth (entrée)", "key": "bluetooth_enabled", "icon": "🔵", "enabled": True},
    {"name": "Jack 3,5 mm", "key": "jack_enabled", "icon": "🔴", "enabled": False},
    {"name": "RCA stéréo", "key": "rca_enabled", "icon": "🟠", "enabled": False},
    {"name": "HDMI audio", "key": "hdmi_enabled", "icon": "🟣", "enabled": False},
    {"name": "Fichier local", "key": "file_enabled", "icon": "📁", "enabled": True}
]

class SourceAudioPage:
    def __init__(self, root, show_home_callback):
        self.root = root
        self.show_home_callback = show_home_callback
        self.widgets = []
        self.current_source = None
        self.config = load_config()
        self.frame = tk.Frame(root, bg=COULEUR_FOND)
        self.build_interface()

    def build_interface(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()

        create_title_label(self.frame, "Sélection de la source audio").pack(pady=5)

        selected_source = self.config.get("audio_input", {}).get("source", "Bluetooth (entrée)")

        for source in AUDIO_SOURCES:
            icon = source["icon"]
            name = source["name"]
            enabled = source["enabled"]

            row = tk.Frame(self.frame, bg=COULEUR_FOND)
            row.pack(fill='x', pady=2)

            label = tk.Label(row, text=f"{icon} {name}", font=FONT_STANDARD, fg=COULEUR_TEXTE, bg=COULEUR_FOND, anchor="w")
            label.pack(side="left", padx=10, fill="x", expand=True)

            if enabled:
                btn_text = "Choisir" if name != selected_source else "✔️ Sélectionné"
                button = create_button(row, btn_text, lambda s=name: self.set_source(s))
                button.pack(side="right", padx=10)
            else:
                button = tk.Label(row, text="En option", font=FONT_STANDARD, fg="gray", bg=COULEUR_FOND)
                button.pack(side="right", padx=10)

            self.widgets.extend([label, button, row])

            if name == "Fichier local" and enabled:
                browse_btn = create_button(self.frame, "📁 Choisir un fichier", self.browse_file)
                browse_btn.pack(pady=4)
                self.widgets.append(browse_btn)

        create_separator(self.frame).pack(pady=5)

        btn_retour = create_button(self.frame, "Retour", self.show_home_callback)
        btn_retour.pack(pady=5)
        self.widgets.append(btn_retour)

        self.frame.pack(fill="both", expand=True)

    def set_source(self, source_name):
        self.config["audio_input"] = {
            "source": source_name
        }
        save_config(self.config)
        self.build_interface()

    def browse_file(self):
        filepath = filedialog.askopenfilename(
            title="Sélectionner un fichier audio",
            filetypes=[("Fichiers audio", "*.wav *.mp3 *.flac")],
            initialdir="/home/pi/Music"
        )
        if filepath:
            self.config["audio_input"] = {
                "source": "Fichier local",
                "filepath": filepath
            }
            save_config(self.config)
            self.build_interface()

    def destroy(self):
        for widget in self.widgets:
            widget.destroy()
        self.frame.destroy()
