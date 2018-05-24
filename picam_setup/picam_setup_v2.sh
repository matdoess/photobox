#!/bin/bash

# If you have not enabled camera, enable it with raspi-config then reboot
#sudo raspi-config

# Install dependencies
sudo apt-get update
sudo apt-get install libharfbuzz0b libfontconfig1

# Optionally, increase microphone volume with alsamixer
read -p "Optionally, increase microphone volume with alsamixer. Press ENTER to continue."
alsamixer

# Install picam binary
wget https://github.com/iizukanao/picam/releases/download/v1.4.6/picam-1.4.6-binary-stretch.tar.xz
tar xvf picam-1.4.6-binary-stretch.tar.xz
mkdir ~/picam
cp picam-1.4.6-binary-stretch/picam ~/picam/
