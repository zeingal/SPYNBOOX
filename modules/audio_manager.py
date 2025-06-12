import subprocess
from modules import config, logger

# Commande de base pour lecture audio avec ffplay (ou ffmpeg selon install)
FFPLAY_CMD = "ffplay -nodisp -autoexit -volume {volume} -af {filter} {file}"

def build_equalizer_filter(eq_settings):
    # Crée la chaîne de filtres d’égalisation pour ffplay
    bass = eq_settings.get("bass", 0)
    mid = eq_settings.get("mid", 0)
    treble = eq_settings.get("treble", 0)
    return f"equalizer=f=100:t=q:w=1:g={bass},equalizer=f=1000:t=q:w=1:g={mid},equalizer=f=10000:t=q:w=1:g={treble}"

def play_audio(file_path, output_index):
    cfg = config.load_config()
    volume = cfg["volume_outputs"][output_index]
    eq_filter = build_equalizer_filter(cfg["equalizer"])

    try:
        command = FFPLAY_CMD.format(
            volume=volume,
            filter=eq_filter,
            file=file_path
        ).split()

        logger.log_info(f"Lancement lecture audio sortie {output_index} : {file_path}")
        subprocess.Popen(command)
    except Exception as e:
        logger.log_error(f"Erreur lecture audio sortie {output_index} : {e}")
