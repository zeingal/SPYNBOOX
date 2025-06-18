# modules/equalizer.py

import json
import os
from tkinter import Frame, Label, Scale, HORIZONTAL
from modules.logging import log
from modules.pages_utils import create_label
from modules.equalizer_config import CONFIG_FILE


def load_equalizer_settings():
    """Charge les réglages de l'égaliseur depuis config.json"""
    if not os.path.exists(CONFIG_FILE):
        log("Fichier config.json introuvable, valeurs par défaut utilisées.")
        return {"bass": 0, "mid": 0, "treble": 0}

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            eq = config.get("equalizer", {"bass": 0, "mid": 0, "treble": 0})
            return eq
    except Exception as e:
        log(f"[EQ] Erreur chargement : {e}")
        return {"bass": 0, "mid": 0, "treble": 0}


def save_equalizer_settings(bass, mid, treble):
    """Enregistre les réglages de l'égaliseur dans config.json"""
    config = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
        except Exception as e:
            log(f"[EQ] Erreur lecture pour sauvegarde : {e}")

    config["equalizer"] = {
        "bass": bass,
        "mid": mid,
        "treble": treble
    }

    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
            log("[EQ] Réglages enregistrés avec succès.")
    except Exception as e:
        log(f"[EQ] Erreur sauvegarde : {e}")


def create_equalizer_page(parent, output_name):
    """Crée l’interface de l’égaliseur pour une sortie donnée"""
    eq_frame = Frame(parent, bg="#222", padx=10, pady=10)
    create_title_label(eq_frame, f"Égaliseur - {output_name}")

    settings = load_equalizer_settings()

    sliders = {}

    def create_slider(name, row, value):
        Label(eq_frame, text=name, bg="#222", fg="white").grid(row=row, column=0, sticky="w")
        slider = Scale(eq_frame, from_=-10, to=10, orient=HORIZONTAL, bg="#333", fg="orange",
                       troughcolor="#444", highlightthickness=0)
        slider.set(value)
        slider.grid(row=row, column=1, padx=10)
        sliders[name] = slider

    create_slider("bass", 1, settings.get("bass", 0))
    create_slider("mid", 2, settings.get("mid", 0))
    create_slider("treble", 3, settings.get("treble", 0))

    def save():
        bass = sliders["bass"].get()
        mid = sliders["mid"].get()
        treble = sliders["treble"].get()
        save_equalizer_settings(bass, mid, treble)

    # Bouton "Enregistrer" stylé SPYNBOOX
    from tkinter import Button
    Button(eq_frame, text="Enregistrer", command=save, bg="#FF6600", fg="white", padx=10).grid(row=4, column=0, columnspan=2, pady=10)

    return eq_frame


def set_equalizer(band, value):
    """Met à jour la valeur d'une bande de l'égaliseur dans le fichier de config"""
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        config.setdefault("equalizer", {})[band] = value
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        log(f"[EQ] {band} réglé sur {value}")
    except Exception as e:
        log(f"[ERREUR] set_equalizer échoué : {e}")


def reset_equalizer():
    """Réinitialise toutes les bandes de l’égaliseur à 0"""
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
        config["equalizer"] = {"bass": 0, "mid": 0, "treble": 0}
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        log("[EQ] Égaliseur réinitialisé à 0")
    except Exception as e:
        log(f"[ERREUR] reset_equalizer échoué : {e}")
