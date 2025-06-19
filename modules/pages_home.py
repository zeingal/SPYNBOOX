import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # Sécurité sur les couleurs
    background = COLORS.get("background", "#FFFFFF")
    accent = COLORS.get("accent", "#000000")
    button_bg = COLORS.get("button", "#4CAF50")
    button_fg = COLORS.get("button_text", "#FFFFFF")

    # Cadre principal
    main_frame = create_frame(root, bg="#202020")  # au lieu de COLORS["background"]
    main_frame.pack(expand=True, fill="both")

    # Titre
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS["title"],
        fg=accent,
        bg=background
    ).pack(pady=10)

    # Cadre pour grille de boutons
    grid_frame = tk.Frame(main_frame, bg="#202020")
    grid_frame.pack(pady=10)

    # Boutons à afficher (page, label, emoji)
    buttons = [
        ("audio", "Audio", "🎧"),
        ("equalizer", "Égaliseur", "🎚️"),
        ("bluetooth", "Bluetooth", "📡"),
        ("settings", "Paramètres", "⚙️"),
        ("shutdown", "Éteindre", "⏻"),
        (None, "", "")  # Case vide pour équilibrer
    ]

    # Affichage en grille 2x3
    for index, (page_name, label, emoji) in enumerate(buttons):
        row = index // 2
        col = index % 2
        if page_name:
            btn = create_button(
                grid_frame,
                text=f"{emoji} {label}",
                command=lambda p=page_name: navigate_callback(p),
                bg=button_bg,
                fg=button_fg,
                font=FONTS["button"]
            )
        else:
            # Bouton inactif invisible mais occupe l’espace
            btn = tk.Label(grid_frame, text="", bg=background)

        btn.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=5)
