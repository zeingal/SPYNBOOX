# modules/pages_shutdown.py

from modules.pages_utils import create_label, create_button, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.system import shutdown_device

def create_shutdown_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    frame = create_frame(root, bg=COLORS["background"])
    frame.pack(expand=True, fill="both")

    create_label(
        frame,
        text="⚠️ Éteindre l’appareil ?",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=20)

    create_button(
        frame,
        text="🛑 Confirmer l’arrêt",
        command=shutdown_device,
        bg="red",
        fg="white",
        font=FONTS["button"]
    ).pack(pady=10)

    create_button(
        frame,
        text="↩️ Annuler",
        command=lambda: navigate_callback("home"),
        bg=COLORS["return"],
        fg=COLORS["button_text"],
        font=FONTS["button"]
    ).pack(pady=10)
