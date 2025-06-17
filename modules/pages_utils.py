import tkinter as tk

# === Paramètres graphiques globaux ===
FONT_DEFAULT = ("Bungee", 12)
COLOR_BUTTON = "#FF6600"  # Orange
COLOR_BUTTON_TEXT = "white"
COLOR_LABEL = "#333333"
COLOR_BACKGROUND = "#F0F0F0"
COLOR_SLIDER = "#FF6600"
SLIDER_LENGTH = 200


# === Bouton stylisé ===
def create_button(parent, text, command=None, width=15):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=FONT_DEFAULT,
        bg=COLOR_BUTTON,
        fg=COLOR_BUTTON_TEXT,
        activebackground="#cc5200",
        relief="raised",
        bd=2,
        width=width
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


# === Slider avec étiquette centrée ===
def create_labeled_slider(parent, label_text, from_, to, command=None):
    frame = tk.Frame(parent, bg=COLOR_BACKGROUND)
    
    label = create_label(frame, label_text)
    label.pack(pady=(0, 5))

    slider = tk.Scale(
        frame,
        from_=from_,
        to=to,
        orient="vertical",
        length=SLIDER_LENGTH,
        sliderlength=15,
        showvalue=True,
        tickinterval=(to - from_) // 2,
        fg=COLOR_LABEL,
        bg=COLOR_BACKGROUND,
        troughcolor="#DDDDDD",
        activebackground=COLOR_SLIDER,
        font=FONT_DEFAULT,
        command=command
    )
    slider.pack()

    return frame, slider


# === Cadre standard pour page ou section ===
def create_frame(parent, padding=10):
    return tk.Frame(parent, bg=COLOR_BACKGROUND, padx=padding, pady=padding)


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
        command=command
    )
    return slider
