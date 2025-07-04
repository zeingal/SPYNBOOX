import tkinter as tk

# === Paramètres graphiques globaux ===
FONT_DEFAULT = ("Bungee", 12)
COLOR_BUTTON = "#4CAF50"
COLOR_BUTTON_TEXT = "white"
COLOR_LABEL = "#333333"
COLOR_BACKGROUND = "#F0F0F0"
COLOR_SLIDER = "#FF6600"
SLIDER_LENGTH = 200

# === Bouton stylisé ===
def create_button(parent, text, command=None, width=15, bg=None, fg=None, font=None):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        bg=bg if bg else COLOR_BUTTON,
        fg=fg if fg else COLOR_BUTTON_TEXT,
        font=font if font else FONT_DEFAULT,
        activebackground="#cc5200",
        relief="raised",
        bd=2,
    )

# === Label stylisé ===
def create_label(parent, text, font=FONT_DEFAULT, fg=COLOR_LABEL, bg=COLOR_BACKGROUND):
    return tk.Label(
        parent,
        text=text,
        font=font,
        fg=fg,
        bg=bg
    )

# === Frame avec fond personnalisé ===
def create_frame(parent, padding=10, bg=None):
    return tk.Frame(parent, bg=bg or COLOR_BACKGROUND, padx=padding, pady=padding)

# === Bouton Retour standard ===
def create_back_button(parent, command=None):
    return create_button(parent, "Retour", command=command, width=10)

# === Slider simple sans étiquette ===
def create_slider(parent, from_=0, to=100, command=None, orient=tk.HORIZONTAL):
    slider = tk.Scale(
        parent,
        from_=from_,
        to=to,
        orient=orient,
        length=SLIDER_LENGTH,
        fg=COLOR_LABEL,
        bg=COLOR_BACKGROUND,
        troughcolor="#DDDDDD",
        activebackground=COLOR_SLIDER,
        font=FONT_DEFAULT,
        command=command,
        sliderlength=20  # ✅ plus large
    )
    return slider

# === Slider avec étiquette centrée ===
def create_labeled_slider(parent, label_text, from_, to, command=None):
    frame = tk.Frame(parent, bg=COLOR_BACKGROUND)

    label = create_label(frame, label_text)
    label.pack(pady=(0, 5))

    slider = create_slider(frame, from_=from_, to=to, command=command)
    slider.pack()

    return frame

# === Séparateur horizontal standard ===
def create_separator(parent):
    separator = tk.Frame(parent, height=2, bd=0, relief="flat", bg="#AAAAAA")
    return separator
