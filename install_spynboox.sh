#!/bin/bash

echo "🔧 Installation des dépendances SPYNBOOX..."

# Mise à jour système
sudo apt update && sudo apt upgrade -y

# Dépendances système
sudo apt install -y python3-pip python3-pil python3-tk python3-setuptools python3-numpy \
blueman bluez pulseaudio pavucontrol sox \
libatlas-base-dev espeak-ng vlc git

# Lancer PulseAudio
pulseaudio --start

# Ajouter l’utilisateur au groupe bluetooth
sudo usermod -aG bluetooth pi

# Ajouter la variable d’environnement PulseAudio si absente
if ! grep -q "PULSE_SERVER=127.0.0.1" ~/.bashrc; then
  echo "export PULSE_SERVER=127.0.0.1" >> ~/.bashrc
fi

# Installer les modules Python
pip3 install --upgrade pip
pip3 install pybluez psutil pygame pillow numpy

# Créer les dossiers de ressources
mkdir -p Assets/sounds
mkdir -p Assets/images
mkdir -p Assets/fonts
mkdir -p Assets/animations

echo ""
echo "✅ Tous les paquets sont installés avec succès."
echo "🔁 Redémarrage conseillé pour tout activer."
echo ""
echo "➡️  Tu peux ensuite lancer SPYNBOOX avec :"
echo "    python3 main.py"
