#!/bin/bash

# Instalar Google Chrome estable (última versión estable)
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Mostrar versión instalada
CHROME_VERSION=$(google-chrome --version)
echo "Versión de Chrome instalada: $CHROME_VERSION"

# Descargar y configurar ChromeDriver versión 137.0.7151.55 (compatible con Chrome 137)
CHROMEDRIVER_VERSION="137.0.7151.55"

wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
mv chromedriver-linux64/chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

echo "Chrome y ChromeDriver instalados correctamente"
