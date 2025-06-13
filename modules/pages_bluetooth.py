import tkinter as tk
from modules.pages_utils import create_label, create_button, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.bluetooth_outputs import list_nearby_devices, pair_device_to_output

def create_bluetooth_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    frame = create_frame(root, bg=COLORS["background"])
    frame.pack(expand=True, fill="both")

    # Titre compact
    create_label(
        frame,
        text="🔵 Appairage BT",
        font=FONTS["title"],
        fg=COLORS["accent"],
        bg=COLORS["background"]
    ).pack(pady=5)

    # Menu de sélection de sortie
    selected_output = tk.StringVar(value="1")
    outputs = ["1", "2", "3"]
    output_menu = tk.OptionMenu(frame, selected_output, *outputs)
    output_menu.config(font=FONTS["small"])
    output_menu.pack(pady=2)

    # Liste des appareils détectés
    device_listbox = tk.Listbox(
        frame,
        font=FONTS["tiny"],
        width=30,
        height=5,
        selectmode=tk.SINGLE
    )
    device_listbox.pack(pady=2)

    # Fonctions de scan et appairage
    def refresh_devices():
        device_listbox.delete(0, tk.END)
        nearby = list_nearby_devices()
        for device in nearby:
            device_listbox.insert(tk.END, f"{device['name']} ({device['mac']})")

    def pair_selected():
        selected = device_listbox.curselection()
        if selected:
            device_info = device_listbox.get(selected[0])
            mac = device_info.split("(")[-1].replace(")", "").strip()
            pair_device_to_output(mac, int(selected_output.get()))

    # Boutons en ligne
    btn_frame = create_frame(frame, bg=COLORS["background"])
    btn_frame.pack(pady=5)

    create_button(
        btn_frame,
        text="🔍",
        command=refresh_devices,
        font=FONTS["icon"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    ).pack(side="left", padx=4)

    create_button(
        btn_frame,
        text="🔗",
        command=pair_selected,
        font=FONTS["icon"],
        bg=COLORS["accent"],
        fg=COLORS["button_text"]
    ).pack(side="left", padx=4)

    create_button(
        btn_frame,
        text="⬅️",
        command=lambda: navigate_callback("home"),
        font=FONTS["icon"],
        bg=COLORS["return"],
        fg=COLORS["button_text"]
    ).pack(side="left", padx=4)
