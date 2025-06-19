import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # === Sécurisation des couleurs ===
    background = COLORS.get("background", "#000000")
    accent = COLORS.get("accent", "#00BFFF")
    button_bg = COLORS.get("button", "#4CAF50")
    button_fg = COLORS.get("button_text", "#FFFFFF")

    # === Cadre principal ===
    main_frame = create_frame(root, bg=background)
    main_frame.pack(expand=True, fill="both")

    # === Titre ===
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS.get("title", ("Arial", 20, "bold")),
        fg=accent,
        bg=background
    ).pack(pady=10)

    # === Grille de boutons ===
    grid_frame = tk.Frame(main_frame, bg=background)
    grid_frame.pack(expand=True)

    buttons = [
        ("audio", "Audio", "🎧"),
        ("equalizer", "Égaliseur", "🎚️"),
        ("bluetooth", "Bluetooth", "📡"),
        ("settings", "Paramètres", "⚙️"),
        ("shutdown", "Éteindre", "⏻"),
        ("none", "", "")  # bouton vide pour équilibre visuel
    ]

    for index, (page_name, label, emoji) in enumerate(buttons):
        row, col = divmod(index, 2)
        if page_name != "none":
            btn = create_button(
                grid_frame,
                text=f"{emoji} {label}",
                command=lambda p=page_name: navigate_callback(p),
                bg=button_bg,
                fg=button_fg,
                font=FONTS.get("button", ("Arial", 12))
            )
        else:
            btn = tk.Label(grid_frame, text="", bg=background)

        btn.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=5)
