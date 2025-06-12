import subprocess

def set_brightness(level):
    """
    Ajuste la luminosité de l’écran entre 0 (éteint) et 255 (max)
    """
    level = max(0, min(255, int(level)))
    try:
        subprocess.run(['sudo', 'tee', '/sys/class/backlight/*/brightness'], input=str(level), text=True)
        print(f"[SPYNBOOX] Luminosité réglée sur {level}")
    except Exception as e:
        print(f"[SPYNBOOX] Erreur de réglage de luminosité : {e}")

def get_brightness():
    """
    Lit la luminosité actuelle de l’écran
    """
    try:
        result = subprocess.check_output(['cat', '/sys/class/backlight/*/brightness'], text=True)
        return int(result.strip())
    except Exception as e:
        print(f"[SPYNBOOX] Erreur de lecture de luminosité : {e}")
        return 128  # Valeur par défaut
