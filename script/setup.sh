#!/bin/bash

### System Basics ###
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install synaptic xscreensaver

### Photobox ###
# Schriften
sudo apt-get install fonts-yanone-kaffeesatz ttf-staypuft
# Software
sudo apt-get install imagemagick ffmpeg

### Nice to Have ###
sudo apt-get install gimp

### Kivy ###
# https://kivy.org/docs/installation/installation-rpi.html
# Dependencies:
sudo apt-get update
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip

# Install a new enough version of Cython
sudo pip install -U Cython==0.25.2
sudo pip3 install -U Cython==0.25.2

# Install Kivy globally on your system
sudo pip install git+https://github.com/kivy/kivy.git@master
sudo pip3 install git+https://github.com/kivy/kivy.git@master

### Python Module ###
# Wand (ImageMagick API)
sudo pip install Wand
sudo pip3 install Wand
sudo apt-get install libmagickwand-dev

# Telegram Bot
sudo pip3 install python-telegram-bot

# Bluetooth
sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez
sudo pip3 install pybluez
sudo pip3 install PyOBEX
