#!/bin/bash

# Actualizar paquetes primero
apt-get update

# Instalar wget y unzip por si no están
apt-get install -y wget unzip

# Descargar e instalar Google Chrome estable versión 137
wget -q https://storage.googleapis.com/chrome-for-testing/137.0.7151.56/linux64/chrome-linux64.zip
unzip -o chrome-linux64.zip -d /usr/bin/
chmod +x /usr/bin/chrome-linux64/chrome

# Descargar ChromeDriver versión 137.0.7151.56
wget -q https://chromedriver.storage.googleapis.com/137.0.7151.56/chromedriver-linux64.zip
unzip -o chromedriver-linux64.zip -d /usr/bin/
chmod +x /usr/bin/chromedriver-linux64/chromedriver

echo "Chrome y ChromeDriver versión 137 instalados correctamente"
