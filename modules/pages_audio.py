
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

    create_label(
        main_frame,
        text="🎛️ Contrôle Audio",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=5)

    # === Ligne 1 : PLAY / STOP / vumètre ===
    line1 = create_frame(main_frame, bg=COLORS["background"])
    line1.pack(pady=5)

    create_button(
        line1,
        text="▶️",
        command=start_playback,
        bg="green",
        fg="white",
        font=FONTS["button"],
        width=5
    ).pack(side="left", padx=2)

    create_button(
        line1,
        text="⏹️",
        command=lambda: [stop_playback(), vumeter.set(0)],
        bg="green",
        fg="white",
        font=FONTS["button"],
        width=5
    ).pack(side="left", padx=2)

    vumeter = tk.Scale(
        line1,
        from_=0,
        to=100,
        orient="horizontal",
        length=100,
        state="disabled",
        sliderlength=10,
        bg=COLORS["background"],
        highlightthickness=0,
        troughcolor=COLORS["slider_trough"],
        fg=COLORS["accent"]
    )
    vumeter.set(0)
    vumeter.pack(side="left", padx=2)

    def update_vumeter():
        if is_playing():
            vumeter.set(random.randint(20, 100))
        else:
            vumeter.set(0)
        root.after(200, update_vumeter)

    update_vumeter()

    # === Sorties Bluetooth (3 lignes) ===
    for i in range(1, 4):
        create_output_line(main_frame, i, navigate_callback)

    # Bouton retour
    create_button(
        main_frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("home"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=5)

def create_output_line(parent, index, navigate_callback):
    frame = create_frame(parent, bg=COLORS["background"])
    frame.pack(pady=4)

    # Appairage
    connected = is_output_connected(index)
    color = COLORS["green"] if connected else COLORS["red"]
    create_button(
        frame,
        text="🔗",
        command=lambda: pair_device_to_output(index),
        bg=color,
        fg="white",
        font=FONTS["mini"],
        width=2
    ).pack(side="left", padx=2)

    # Slider volume
    create_slider(
        frame,
        from_=0,
        to=100,
        initial=50,
        command=lambda val: print(f"[SPYNBOOX] Volume {index}: {val}"),
        length=100
    ).pack(side="left", padx=3)

    # EQ
    create_button(
        frame,
        text="🎚️",
        command=lambda: create_equalizer_page(parent, navigate_callback, index),
        bg=COLORS["button"],
        fg=COLORS["button_text"],
        font=FONTS["mini"],
        width=2
    ).pack(side="left", padx=2)

    # Mode ST/D/G
    config = load_config()
    mode = config.get("bluetooth_outputs", {}).get(f"output{index}", {}).get("mode", "ST")
    create_button(
        frame,
        text=mode,
        command=lambda: create_mode_selection_page(parent, navigate_callback, index),
        bg=COLORS["button"],
        fg=COLORS["button_text"],
        font=FONTS["mini"],
        width=3
    ).pack(side="left", padx=2)

    # TEST
    create_button(
        frame,
        text="🔊",
        command=lambda: play_sound_file(TEST_SOUND_PATH, index),
        bg=COLORS["button"],
        fg=COLORS["button_text"],
        font=FONTS["mini"],
        width=2
    ).pack(side="left", padx=2)
