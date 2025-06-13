import tkinter as tk
from modules.pages_utils import create_label, create_button, create_slider, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.config_manager import load_config, save_config
from modules.rtc import set_manual_time, auto_sync_time
from modules.system import update_system  # On n'importe plus shutdown_device ici

def create_settings_page(root, navigate_callback, apply_theme_callback, set_brightness_callback):
    config = load_config()
    theme = config.get("theme", "day")
    brightness = config.get("brightness", 100)

    for widget in root.winfo_children():
        widget.destroy()

    frame = create_frame(root, bg=COLORS["background"])
    frame.pack(expand=True, fill="both", padx=5, pady=5)

    create_label(
        frame,
        text="⚙️ Paramètres Système",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=5)

    # Mode jour/nuit
    def toggle_theme():
        new_theme = "night" if config["theme"] == "day" else "day"
        config["theme"] = new_theme
        save_config(config)
        apply_theme_callback(new_theme)

    theme_button = create_button(
        frame,
        text="🌙 Mode Nuit" if theme == "day" else "☀️ Mode Jour",
        command=toggle_theme,
        font=FONTS["button"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    )
    theme_button.pack(pady=3)

    # Luminosité
    def update_brightness(val):
        config["brightness"] = int(float(val))
        save_config(config)
        set_brightness_callback(config["brightness"])

    create_label(
        frame,
        text="🔆 Luminosité",
        font=FONTS["label"],
        fg=COLORS["foreground"],
        bg=COLORS["background"]
    ).pack()
    create_slider(
        frame,
        from_=0,
        to=100,
        initial=brightness,
        command=update_brightness
    ).pack(pady=3)

    # Réglage de l'heure
    create_button(
        frame,
        text="🕒 Réglage manuel",
        command=set_manual_time,
        font=FONTS["button"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    ).pack(pady=3)

    create_button(
        frame,
        text="🌐 Synchronisation auto",
        command=auto_sync_time,
        font=FONTS["button"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    ).pack(pady=3)

    # Mise à jour système
    create_button(
        frame,
        text="🔄 Mise à jour système",
        command=update_system,
        font=FONTS["button"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    ).pack(pady=3)

    # Redirection vers la page de confirmation d’extinction
    create_button(
        frame,
        text="⏻ Éteindre l’appareil",
        command=lambda: navigate_callback("shutdown"),
        font=FONTS["button"],
        bg="red",
        fg="white"
    ).pack(pady=5)

    # Bouton retour
    create_button(
        frame,
        text="⬅️ Retour",
        command=lambda: navigate_callback("home"),
        font=FONTS["button"],
        bg=COLORS["return"],
        fg=COLORS["button_text"]
    ).pack(pady=5)
