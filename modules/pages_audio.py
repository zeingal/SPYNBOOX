import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.play_sound import play_sound_file, stop_playback

# Exemple de fichier audio à tester
SAMPLE_AUDIO_PATH = "assets/sounds/sample.mp3"

def create_audio_page(root, navigate_callback):
    # Efface les widgets précédents
    for widget in root.winfo_children():
        widget.destroy()

    # Cadre principal
    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True)

    # Titre
    create_label(
        main_frame,
        text="🎵 Contrôle Audio",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=20)

    # Boutons audio
    create_button(
        main_frame,
        text="▶️ Lire un son",
        command=lambda: play_sound_file(SAMPLE_AUDIO_PATH),
        bg=COLORS["button"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=10)

    create_button(
        main_frame,
        text="⏹️ Arrêter la lecture",
        command=stop_playback,
        bg=COLORS["button"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=10)

    # Bouton retour
    create_button(
        main_frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("home"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=30)
