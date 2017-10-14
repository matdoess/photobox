#!/bin/bash

# Run picam
#cd ~/picam
#./picam --alsadev hw:1,0

# Run picam Rotate
#cd ~/picam
#./picam --alsadev hw:1,0 --rotation 180

# Run picam Rotate / Preview / Preview Fullscreen
cd ~/picam
./picam --alsadev hw:1,0 --rotation 180 --hflip --preview --previewrect 0,0,800,480


read -p "Press ENTER to quit."