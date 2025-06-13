import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame, create_slider
from modules.widgets_config import COLORS, FONTS
from modules.equalizer import set_equalizer, reset_equalizer

# Dictionnaire global pour stocker les valeurs des sliders
equalizer_values = {
    "bass": 0,
    "mid": 0,
    "treble": 0
}

def create_equalizer_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True, fill="both")

    create_label(
        main_frame,
        text="🎚️ Égaliseur",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=10)

    # Sous-cadre sliders
    sliders_frame = create_frame(main_frame, bg=COLORS["background"])
    sliders_frame.pack(pady=10)

    def on_slider_change(name, value):
        equalizer_values[name] = int(float(value))
        set_equalizer(**equalizer_values)

    # Basses
    create_label(sliders_frame, text="Basses", font=FONTS["label"], bg=COLORS["background"]).pack()
    bass_slider = create_slider(sliders_frame, from_=-10, to=10, initial=0, command=lambda v: on_slider_change("bass", v))
    bass_slider.pack(pady=5)

    # Médiums
    create_label(sliders_frame, text="Médiums", font=FONTS["label"], bg=COLORS["background"]).pack()
    mid_slider = create_slider(sliders_frame, from_=-10, to=10, initial=0, command=lambda v: on_slider_change("mid", v))
    mid_slider.pack(pady=5)

    # Aigus
    create_label(sliders_frame, text="Aigus", font=FONTS["label"], bg=COLORS["background"]).pack()
    treble_slider = create_slider(sliders_frame, from_=-10, to=10, initial=0, command=lambda v: on_slider_change("treble", v))
    treble_slider.pack(pady=5)

    # Boutons
    create_button(
        main_frame,
        text="🔁 Réinitialiser",
        command=lambda: reset_all_sliders(bass_slider, mid_slider, treble_slider),
        bg=COLORS["accent"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=15)

    create_button(
        main_frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("home"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=10)

def reset_all_sliders(bass_slider, mid_slider, treble_slider):
    bass_slider.set(0)
    mid_slider.set(0)
    treble_slider.set(0)
    reset_equalizer()
