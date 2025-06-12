# modules/start_animation.py

import tkinter as tk

def play_start_animation(root, callback):
    canvas = tk.Canvas(root, width=480, height=320, bg="black", highlightthickness=0)
    canvas.pack()

    logo = canvas.create_text(240, 160, text="SPYNBOOX", font=("Bungee", 10), fill="white")

    def enlarge_logo(step=0):
        if step <= 10:
            size = 10 + step * 5
            canvas.itemconfig(logo, font=("Bungee", size))
            root.after(200, lambda: enlarge_logo(step + 1))
        else:
            root.after(300, callback)

    enlarge_logo()

def end_animation(canvas):
    canvas.delete("all")
