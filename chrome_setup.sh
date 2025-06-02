#!/bin/bash

# Actualizar paquetes e instalar wget y unzip por si no están
apt-get update
apt-get install -y wget unzip

# Descargar e instalar Google Chrome estable
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Descargar y descomprimir ChromeDriver versión 114.0.5735.90 (compatible con Chrome estable)
wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

echo "Chrome y ChromeDriver instalados correctamente"
