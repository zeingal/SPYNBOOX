import os
import tkinter as tk
from tkinter import messagebox
import threading
import pygame

pygame.init()

def show_popup(title, message):
    """
    Affiche une popup tkinter avec un titre et un message.
    """
    def popup():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title, message)
        root.destroy()
    threading.Thread(target=popup).start()

def play_notification_sound(sound_file):
    """
    Joue un son de notification (.wav ou .mp3).
    """
    try:
        if os.path.exists(sound_file):
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        else:
            print(f"[NOTIF] Fichier introuvable : {sound_file}")
    except Exception as e:
        print(f"[NOTIF] Erreur lecture son : {e}")
