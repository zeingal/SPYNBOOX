import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # === Couleurs ===
    background = COLORS.get("background", "#000000")
    accent = COLORS.get("accent", "#00BFFF")
    button_bg = COLORS.get("button", "#4CAF50")
    button_fg = COLORS.get("button_text", "#FFFFFF")

    # Cadre principal
    main_frame = create_frame(root, bg=background)
    main_frame.pack(expand=True, fill="both")

    # Titre
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS.get("title", ("Arial", 18, "bold")),
        fg=accent,
        bg=background
    ).pack(pady=20)

    # Grille de boutons
    grid_frame = tk.Frame(main_frame, bg=background)
    grid_frame.pack()

    # Liste des boutons
    buttons = [
        ("audio",      "Audio",       "🎧"),
        ("equalizer",  "Égaliseur",   "🎚️"),
        ("bluetooth",  "Bluetooth",   "📡"),
        ("settings",   "Paramètres",  "⚙️"),
        ("shutdown",   "Éteindre",    "⏻"),
        ("inactive",   "",            "")  # faux bouton vide
    ]

    for index, (page_name, label, emoji) in enumerate(buttons):
        row = index // 2
        col = index % 2

        if page_name == "inactive":
            btn = tk.Button(
                grid_frame,
                text="",
                bg=button_bg,
                state="disabled",
                relief="raised",
                width=16,
                height=2
            )
        else:
            btn = tk.Button(
                grid_frame,
                text=f"{emoji} {label}",
                command=lambda p=page_name: navigate_callback(p),
                bg=button_bg,
                fg=button_fg,
                font=FONTS.get("button", ("Arial", 12)),
                relief="raised",
                width=16,
                height=2
            )

        btn.grid(row=row, column=col, padx=20, pady=10)
