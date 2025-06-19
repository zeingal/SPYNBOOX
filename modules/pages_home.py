
import tkinter as tk
from modules.pages_utils import create_button, create_label, create_frame
from modules.widgets_config import COLORS, FONTS

def display_home_page(root, navigate_callback):
    # Nettoyage de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # === Sécurisation des couleurs ===
    background = COLORS.get("background", "#000000")      # fond noir par défaut
    accent = COLORS.get("accent", "#00BFFF")              # bleu par défaut
    button_bg = COLORS.get("button", "#4CAF50")           # vert
    button_fg = COLORS.get("button_text", "#FFFFFF")      # blanc

    # Cadre principal
    main_frame = create_frame(root, bg=background)
    main_frame.pack(expand=True, fill="both")

    # Titre SPYNBOOX
    create_label(
        main_frame,
        text="SPYNBOOX",
        font=FONTS.get("title", ("Arial", 18, "bold")),
        fg=accent,
        bg=background
    ).pack(pady=20)

    # Cadre pour grille de boutons
    grid_frame = tk.Frame(main_frame, bg=background)
    grid_frame.pack()

    # Liste des boutons à afficher (6 éléments pour 3x2)
    buttons = [
        ("audio",      "Audio",       "🎧"),
        ("equalizer",  "Égaliseur",   "🎚️"),
        ("bluetooth",  "Bluetooth",   "📡"),
        ("settings",   "Paramètres",  "⚙️"),
        ("shutdown",   "Éteindre",    "⏻"),
        ("placeholder", "", "")  # bouton vide, esthétique
    ]

    # Création en grille 2 colonnes
    for index, (page_name, label, emoji) in enumerate(buttons):
        row = index // 2
        col = index % 2

        if page_name == "placeholder":
            # Faux bouton vide mais même taille
            btn = tk.Label(
                grid_frame,
                text="",
                bg=button_bg,
                width=16,
                height=2,
                relief="raised",
                bd=2
            )
        else:
            btn = create_button(
                grid_frame,
                text=f"{emoji} {label}",
                command=lambda p=page_name: navigate_callback(p),
                bg=button_bg,
                fg=button_fg,
                font=FONTS.get("button", ("Arial", 12))
            )

        btn.grid(row=row, column=col, padx=20, pady=10)
