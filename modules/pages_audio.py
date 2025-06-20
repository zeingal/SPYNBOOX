
import tkinter as tk
import random
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

TEST_SOUND_PATH = "assets/sounds/boom.wav"

def create_audio_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True, fill="both")

    create_label(
        main_frame, text="Contrôle Audio", font=FONTS["title"],
        fg=COLORS["accent"], bg=COLORS["background"]
    ).pack(pady=5)

    # Ligne 1 : PLAY / STOP + vumètre
    playback_frame = create_frame(main_frame, bg=COLORS["background"])
    playback_frame.pack(pady=5)

    create_button(
        playback_frame, text="▶️", command=start_playback,
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["button"]
    ).pack(side="left", padx=5)

    create_button(
        playback_frame, text="⏹️", command=lambda: stop_playback(),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["button"]
    ).pack(side="left", padx=5)

    vumeter = tk.Scale(
        playback_frame, from_=0, to=100, orient="horizontal", length=100,
        state="disabled", sliderlength=10, bg=COLORS["background"],
        fg=COLORS["accent"], highlightthickness=0, troughcolor="#333333"
    )
    vumeter.set(0)
    vumeter.pack(side="left", padx=5)

    def update_vumeter():
        if is_playing():
            vumeter.set(random.randint(20, 100))
        else:
            vumeter.set(0)
        root.after(200, update_vumeter)

    update_vumeter()

    # Lignes 2 à 4 : Contrôles par sortie
    for output_index in range(1, 4):
        create_output_controls(main_frame, output_index, navigate_callback)

def create_output_controls(parent, output_index, navigate_callback):
    frame = create_frame(parent, bg=COLORS["background"])
    frame.pack(pady=3)

    connected = is_output_connected(output_index)
    pair_color = "green" if connected else "red"

    # Bouton d'appairage (LED verte/rouge)
    create_button(
        frame, text=" ", bg=pair_color, fg="white", width=2,
        command=lambda: navigate_callback("bluetooth")
    ).pack(side="left", padx=3)

    # Slider de volume
    create_slider(
        frame, from_=0, to=100, initial=50,
        command=lambda val: print(f"[SPYNBOOX] Volume sortie {output_index} : {val}"),
        length=100
    ).pack(side="left", padx=5)

    # Bouton EQ
    create_button(
        frame, text="EQ",
        command=lambda: create_equalizer_page(parent, navigate_callback, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=2)

    # Bouton ST/D/G
    config = load_config()
    mode = config.get("bluetooth_outputs", {}).get(f"output{output_index}", {}).get("mode", "ST")
    create_button(
        frame, text=mode,
        command=lambda: create_mode_selection_page(parent, navigate_callback, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=2)

    # Bouton TEST
    create_button(
        frame, text="Test",
        command=lambda: play_sound_file(TEST_SOUND_PATH, output_index),
        bg=COLORS["button"], fg=COLORS["button_text"], font=FONTS["mini"]
    ).pack(side="left", padx=2)
