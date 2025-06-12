import tkinter as tk

def play_start_animation(root, callback):
    canvas = tk.Canvas(root, width=640, height=480, bg="black", highlightthickness=0)
    canvas.place(x=0, y=0)

    logo = canvas.create_text(320, 240, text="SPYNBOOX", fill="white", font=("Bungee", 36))

    def enlarge_logo(step=0):
        if step < 10:
            canvas.itemconfig(logo, font=("Bungee", 36 + step * 4))
            canvas.after(200, lambda: enlarge_logo(step + 1))
        else:
            canvas.after(1000, end_animation)

    def end_animation():
        canvas.destroy()
        callback()

    enlarge_logo()
