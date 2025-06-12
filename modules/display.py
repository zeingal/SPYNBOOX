# modules/display.py

import tkinter as tk
from datetime import datetime
from modules.battery import get_battery_level
from modules.rtc import get_current_time

class DisplayElements:
    def __init__(self, parent):
        self.parent = parent

        self.time_label = tk.Label(parent, text="", font=("Arial", 12), fg="white", bg="black")
        self.time_label.place(x=10, y=10)

        self.battery_label = tk.Label(parent, text="", font=("Arial", 12), fg="white", bg="black")
        self.battery_label.place(x=200, y=10)  # Position à ajuster selon la taille de l'écran

        self.update_display()

    def update_display(self):
        # Récupère l'heure et le niveau de batterie
        current_time = get_current_time()
        battery_level = get_battery_level()

        # Met à jour les labels
        self.time_label.config(text=f"🕒 {current_time}")
        self.battery_label.config(text=f"🔋 {battery_level}%")

        # Rafraîchit toutes les 30 secondes
        self.parent.after(30000, self.update_display)
