import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame, create_slider
from modules.widgets_config import COLORS, FONTS
from modules.equalizer import set_equalizer, reset_equalizer

equalizer_values = {
    "bass": 0,
    "mid": 0,
    "treble": 0
}

def create_equalizer_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    main_frame = create_frame(root, bg=COLORS["background"])
    main_frame.pack(expand=True, fill="both", padx=5, pady=5)

    create_label(
        main_frame,
        text="🎚️ Égaliseur",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=5)

    sliders_frame = create_frame(main_frame, bg=COLORS["background"])
    sliders_frame.pack(pady=5)

    def on_slider_change(name, value):
        equalizer_values[name] = int(float(value))
        set_equalizer(**equalizer_values)

    # Slider compact avec label centré
    for name, label_text in [("bass", "Basses"), ("mid", "Médiums"), ("treble", "Aigus")]:
        create_label(sliders_frame, text=label_text, font=FONTS["label"], bg=COLORS["background"]).pack(pady=1)
        slider = create_slider(
            sliders_frame, from_=-10, to=10, initial=0,
            command=lambda v, n=name: on_slider_change(n, v),
            width=200  # réduit pour écran étroit
        )
        slider.pack(pady=2)

    # Réinitialiser
    create_button(
        main_frame,
        text="🔁 Réinitialiser",
        command=lambda: reset_all_sliders(sliders_frame),
        bg=COLORS["accent"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=5)

    # Retour
    create_button(
        main_frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("home"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=5)

def reset_all_sliders(frame):
    sliders = frame.winfo_children()
    for widget in sliders:
        if isinstance(widget, tk.Scale):
            widget.set(0)
    reset_equalizer()
