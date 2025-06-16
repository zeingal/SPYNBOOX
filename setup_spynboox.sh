#!/bin/bash

echo "🚀 Installation complète de SPYNBOOX en cours..."

# Mise à jour système
echo "📦 Mise à jour des paquets..."
sudo apt update && sudo apt upgrade -y

# Paquets système nécessaires
echo "🔧 Installation des utilitaires système requis..."
sudo apt install -y python3-pip python3-venv git ffmpeg bluez pulseaudio pulseaudio-module-bluetooth python3-tk libatlas-base-dev

# Redémarrage de PulseAudio
echo "🔊 Redémarrage de PulseAudio..."
pulseaudio --start

# Installation des bibliothèques Python
echo "🐍 Installation des librairies Python..."
pip3 install pillow pygame numpy pyserial pybluez

# Librairies pour capteurs RTC DS3231 et INA219
echo "🧠 Installation des drivers RTC et INA219..."
pip3 install adafruit-circuitpython-ds3231 adafruit-circuitpython-ina219

# Activation de l'I2C via raspi-config (non-interactive si script avancé)
echo "📡 Activation de l’I2C (à faire manuellement si besoin)..."
echo "👉 Lancez ensuite : sudo raspi-config → Interfacing Options → I2C → Enable"

# Vérification installation FFMPEG
echo "🎧 Vérification de ffmpeg..."
ffmpeg -version || echo "⚠️ ffmpeg non installé correctement !"

# Instructions post-install
echo ""
echo "✅ Installation terminée !"
echo "➡️ Étapes suivantes recommandées :"
echo "1. Activez l’I2C avec : sudo raspi-config"
echo "2. Redémarrez votre Raspberry Pi : sudo reboot"
echo "3. Lancez SPYNBOOX avec : python3 main.py (ou via un environnement virtuel)"
echo ""
echo "🧠 Conseil : Pour l’audio Bluetooth multipoint, vérifiez que ffmpeg est bien utilisé dans 'playback.py'"
echo "🔁 Vous pouvez maintenant copier votre dossier SPYNBOOX et le tester."
