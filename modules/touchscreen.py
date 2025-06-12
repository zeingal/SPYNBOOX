# modules/touchscreen.py

import tkinter as tk

class TouchInterface:
    def __init__(self, root, on_touch_callback=None):
        self.root = root
        self.on_touch_callback = on_touch_callback
        self.canvas = tk.Canvas(root, width=480, height=320, bg="black", highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_touch)

    def on_touch(self, event):
        x, y = event.x, event.y
        print(f"[TOUCHSCREEN] Touch detected at ({x}, {y})")
        if self.on_touch_callback:
            self.on_touch_callback(x, y)

    def draw_text(self, x, y, text, font=("Arial", 14), fill="white"):
        self.canvas.create_text(x, y, text=text, font=font, fill=fill)

    def clear_screen(self):
        self.canvas.delete("all")
