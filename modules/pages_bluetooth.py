import tkinter as tk
from modules.pages_utils import create_label, create_button, create_frame
from modules.widgets_config import COLORS, FONTS
from modules.bluetooth_outputs import list_nearby_devices, pair_device_to_output

def create_bluetooth_page(root, navigate_callback):
    for widget in root.winfo_children():
        widget.destroy()

    frame = create_frame(root, bg=COLORS["background"])
    frame.pack(expand=True, fill="both")

    create_label(frame, text="🔵 Appairage Bluetooth", font=FONTS["title"], fg=COLORS["accent"], bg=COLORS["background"]).pack(pady=10)

    device_frame = create_frame(frame, bg=COLORS["background"])
    device_frame.pack(pady=10)

    # Dropdown sélection de sortie
    selected_output = tk.StringVar(value="1")
    outputs = ["1", "2", "3"]

    output_menu = tk.OptionMenu(frame, selected_output, *outputs)
    output_menu.config(font=FONTS["label"])
    output_menu.pack(pady=5)

    device_listbox = tk.Listbox(device_frame, font=FONTS["label"], width=40, height=10)
    device_listbox.pack(pady=5)

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

    create_button(frame, text="🔍 Rechercher", command=refresh_devices, font=FONTS["button"], bg=COLORS["accent"], fg=COLORS["button_text"]).pack(pady=5)

    create_button(frame, text="🔗 Appairer", command=pair_selected, font=FONTS["button"], bg=COLORS["accent"], fg=COLORS["button_text"]).pack(pady=5)

    create_button(frame, text="⬅️ Retour", command=lambda: navigate_callback("home"), font=FONTS["button"], bg=COLORS["return"], fg=COLORS["button_text"]).pack(pady=15)
