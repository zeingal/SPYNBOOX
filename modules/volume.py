import subprocess

# Dictionnaire des sinks Bluetooth configurés
# À adapter avec les vrais noms de vos sorties Bluetooth (visible via pactl list sinks short)
SINKS = {
    0: "bluez_output.AA_BB_CC_DD_EE_FF.a2dp-sink",
    1: "bluez_output.11_22_33_44_55_66.a2dp-sink",
    2: "bluez_output.77_88_99_AA_BB_CC.a2dp-sink"
}

def set_volume(output_index, volume):
    """
    Définit le volume pour une sortie audio Bluetooth.
    :param output_index: Index de la sortie (0, 1, 2)
    :param volume: Niveau de volume entre 0.0 et 1.0
    """
    if output_index not in SINKS:
        print(f"[Volume] Index de sortie invalide : {output_index}")
        return

    sink_name = SINKS[output_index]

    try:
        # Convertir le volume en pourcentage
        volume_percent = int(volume * 100)
        cmd = ["pactl", "set-sink-volume", sink_name, f"{volume_percent}%"]
        subprocess.run(cmd, check=True)
        print(f"[Volume] Volume de sortie {output_index} ({sink_name}) défini à {volume_percent}%")
    except subprocess.CalledProcessError as e:
        print(f"[Volume] Erreur lors de la définition du volume pour {sink_name} : {e}")
    except Exception as e:
        print(f"[Volume] Erreur inattendue : {e}")
