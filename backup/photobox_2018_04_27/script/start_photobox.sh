#!/bin/bash

# Hostname exportieren damit in python darauf zugegriffen werden kann
export HOSTNAME


# START Photobox
cd /home/pi/photobox
python3 ScreenManager.py

# Fenster offen lassen
read -p "Press enter to quit"