#!/bin/bash

# image must have a width which is a multiple of 32, and a height which is a multiple of 16. 

### Countdown erstellen

# Variablen
num_start=1
num_end=3
num_font="Yanone-Kaffeesatz-Regular"   # ImageMagick alle Fonts anzeigen [ convert -list font ]
num_size="320x320"
num_pointsize=300

# Script
for num in $(seq $num_start $num_end)
do
convert -size $num_size xc:none -fill white -stroke black \
          -font $num_font -pointsize $num_pointsize -gravity center \
          -draw "text 0,0 '$num'"   img/$num.png
done

### Weißes Bild für Cheese

# Variablen
cheese_size="800x480"
cheese_alpha=j   #j/n Transparenz aktivieren?
cheese_alphaset=80  #Transparenz in Prozent

if [ $cheese_alpha == n ]
then
 convert -size $cheese_size xc:white -define png:color-type=6 img/white.png

elif [ $cheese_alpha == j ]
then
 convert -size $cheese_size xc:white -alpha set -channel Alpha -evaluate set $cheese_alphaset% -define png:color-type=6 img/white.png
else
 echo "Nichts Ausgeführt"
fi

### Script ENDE
read -p "Press enter to quit"