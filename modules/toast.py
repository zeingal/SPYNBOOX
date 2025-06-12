# modules/toast.py

import tkinter as tk
import threading

def show_toast(root, message, duration=2000):
    toast = tk.Toplevel(root)
    toast.overrideredirect(True)
    toast.attributes("-topmost", True)

    # Position centrée sur la fenêtre principale
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    root_width = root.winfo_width()
    root_height = root.winfo_height()

    toast.geometry(f"+{root_x + root_width // 2 - 100}+{root_y + root_height // 2 - 25}")

    label = tk.Label(toast, text=message, bg="black", fg="white", padx=10, pady=5)
    label.pack()

    # Fermer automatiquement après "duration" ms
    toast.after(duration, toast.destroy)
