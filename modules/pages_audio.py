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

    bg = COLORS.get("background", "#000000")
    accent = COLORS.get("accent", "#00FFFF")
    button_bg = COLORS.get("button", "#4CAF50")
    button_fg = COLORS.get("button_text", "#FFFFFF")
    return_bg = COLORS.get("return", "#888888")

    main_frame = create_frame(root, bg=bg)
    main_frame.pack(expand=True, fill="both")

    create_label(
        main_frame,
        text="Contrôle Audio",
        font=FONTS["title"],
        fg=accent,
        bg=bg
    ).pack(pady=5)

    playback_frame = create_frame(main_frame, bg=bg)
    playback_frame.pack(pady=2)

    def open_source_page():
        SourceAudioPage(root, lambda: create_audio_page(root, navigate_callback))

    source_info = get_audio_input_command()
    valid = source_info["type"] in ("file", "stream")
    source_color = "green" if valid else "red"

    create_button(
        playback_frame,
        text="Source",
        command=open_source_page,
        bg=source_color,
        fg="white",
        font=FONTS["button"]
    ).pack(side="left", padx=5)

    create_button(
        playback_frame,
        text="Lecture",
        command=start_playback,
        bg=button_bg,
        fg=button_fg,
        font=FONTS["button"]
    ).pack(side="left", padx=5)

    vumeter = tk.Scale(
        playback_frame,
        from_=0,
        to=100,
        orient="horizontal",
        length=100,
        state="disabled",
        sliderlength=10,
        bg=bg,
        highlightthickness=0,
        troughcolor="#333333",
        fg=accent
    )
    vumeter.set(0)
    vumeter.pack(side="left", padx=5)

    create_button(
        playback_frame,
        text="Stop",
        command=lambda: [stop_playback(), vumeter.set(0)],
        bg=button_bg,
        fg=button_fg,
        font=FONTS["button"]
    ).pack(side="left", padx=5)

    def update_vumeter():
        if is_playing():
            vumeter.set(random.randint(20, 100))
        else:
            vumeter.set(0)
        root.after(200, update_vumeter)

    update_vumeter()

    # 3 lignes de contrôles pour 3 sorties Bluetooth
    for output_index in range(1, 4):
        create_output_controls(main_frame, output_index, navigate_callback)

    create_button(
        main_frame,
        text="Retour",
        command=lambda: navigate_callback("home"),
        bg=return_bg,
        fg=button_fg,
        font=FONTS["button"]
    ).pack(pady=5)


def create_output_controls(parent, output_index, navigate_callback):
    bg = COLORS.get("background", "#000000")
    button_bg = COLORS.get("button", "#4CAF50")
    button_fg = COLORS.get("button_text", "#FFFFFF")
    mini_font = FONTS["mini"]

    frame = create_frame(parent, bg=bg)
    frame.pack(pady=5, fill="x", padx=5)

    connected = is_output_connected(output_index)
    pair_color = "green" if connected else "red"

    create_button(
        frame,
        text="Appairer",
        fg="white",
        bg=pair_color,
        font=FONTS["button"],
        width=8,
        command=lambda: pair_device_to_output(output_index)
    ).pack(side="left", padx=2)

    create_slider(
        frame,
        from_=0,
        to=100,
        initial=50,
        length=100,
        command=lambda val: print(f"[SPYNBOOX] Volume sortie {output_index} : {val}")
    ).pack(side="left", padx=5)

    create_button(
        frame,
        text="EQ",
        command=lambda: create_equalizer_page(parent, navigate_callback, output_index),
        bg=button_bg,
        fg=button_fg,
        font=mini_font
    ).pack(side="left", padx=2)

    config = load_config()
    mode = config.get("bluetooth_outputs", {}).get(f"output{output_index}", {}).get("mode", "ST")

    create_button(
        frame,
        text=mode,
        command=lambda: create_mode_selection_page(parent, navigate_callback, output_index),
        bg=button_bg,
        fg=button_fg,
        font=mini_font
    ).pack(side="left", padx=2)

    create_button(
        frame,
        text="Test",
        command=lambda: play_sound_file(TEST_SOUND_PATH, output_index),
        bg=button_bg,
        fg=button_fg,
        font=mini_font
    ).pack(side="left", padx=2)
