import tkinter as tk
from modules.animation import play_start_animation

def run_app():
    root = tk.Tk()
    root.title("SPYNBOOX")

    def start_main_interface():
        label = tk.Label(root, text="Bienvenue dans SPYNBOOX!", font=("Arial", 16))
        label.pack(pady=20)

    play_start_animation(root, start_main_interface)
    root.mainloop()
