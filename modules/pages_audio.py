
import tkinter as tk
from modules.pages_utils import create_label, create_button, create_slider, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.bluetooth_outputs import is_output_connected, pair_device_to_output
from modules.equalizer import create_equalizer_page
from modules.play_sound import play_sound_file
from modules.modes import create_mode_selection_page
from modules.playback import start_playback, stop_playback, is_playing
from modules.audio_input import get_audio_input_command
from modules.pages_source_audio import SourceAudioPage
from modules.config_manager import load_config

import random

TEST_SOUND_PATH = "assets/sounds/boom.wav"

def create_audio_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True, fill="both")

    # Titre
    create_label(
        main_frame, text="🎛️ Contrôle Audio", font=FONTS["title"],
        fg=COLORS["accent"], bg=COLORS["background"]
    ).pack(pady=5)

    # --- LIGNE 1 : Contrôle source ---
    control_frame = create_frame(main_frame, bg=COLORS["background"])
    control_frame.pack(pady=5)

    create_button(
        control_frame, text="▶️ Lecture", command=start_playback,
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["button"]
    ).pack(side="left", padx=5)

    create_button(
        control_frame, text="⏹️ Stop", command=lambda: [stop_playback(), vumeter.set(0)],
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["button"]
    ).pack(side="left", padx=5)

    vumeter = tk.Scale(
        control_frame, from_=0, to=100, orient="horizontal", length=100,
        state="disabled", sliderlength=10,
        bg=COLORS["background"], highlightthickness=0, troughcolor="#333333",
        fg=COLORS["accent"]
    )
    vumeter.set(0)
    vumeter.pack(side="left", padx=5)

    def update_vumeter():
        if is_playing():
            vumeter.set(random.randint(10, 100))
        else:
            vumeter.set(0)
        root.after(300, update_vumeter)

    update_vumeter()

    # --- LIGNES 2 à 4 : Sorties Bluetooth ---
    for i in range(1, 4):
        create_output_controls(main_frame, i, navigate_callback)

    # --- Bouton retour ---
    create_button(
        main_frame, text="⬅️ Retour", command=lambda: navigate_callback("home"),
        bg=COLORS["return"], fg=COLORS["button_text"], font=FONTS["button"]
    ).pack(pady=5)


def create_output_controls(parent, output_index, navigate_callback):
    frame = create_frame(parent, bg=COLORS["background"])
    frame.pack(pady=5, padx=5, fill="x")

    # Appairage
    connected = is_output_connected(output_index)
    pair_color = "green" if connected else "red"
    create_button(
        frame, text="⚙", command=lambda: pair_device_to_output(output_index),
        bg=pair_color, fg="white", font=FONTS["mini"], width=2
    ).pack(side="left", padx=3)

    # Slider volume
    create_slider(
        frame, from_=0, to=100, initial=50,
        command=lambda val: print(f"[SPYNBOOX] Volume sortie {output_index} : {val}"),
        length=100
    ).pack(side="left", padx=5)

    # EQ
    create_button(
        frame, text="🎚️ EQ",
        command=lambda: create_equalizer_page(parent, navigate_callback, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=3)

    # Mode ST/D/G
    config = load_config()
    mode = config.get("bluetooth_outputs", {}).get(f"output{output_index}", {}).get("mode", "ST")
    create_button(
        frame, text=mode,
        command=lambda: create_mode_selection_page(parent, navigate_callback, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=3)

    # Test
    create_button(
        frame, text="🧪 Test",
        command=lambda: play_sound_file(TEST_SOUND_PATH, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=3)
