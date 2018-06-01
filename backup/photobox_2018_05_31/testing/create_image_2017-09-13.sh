#!/bin/bash

#convert -size 100x60 xc:skyblue -fill white -stroke black \
#          -font Yanone-Kaffeesatz-Regular -pointsize 40 -gravity center \
#          -draw "text 0,0 'Hello'"   img/draw_text.gif

# image must have a width which is a multiple of 32, and a height which is a multiple of 16. 

#convert -size 320x320 xc:skyblue -fill white -stroke black \
#          -font Yanone-Kaffeesatz-Regular -pointsize 300 -gravity center \
#          -draw "text 0,0 '3'"   img/3.png

convert -size 320x320 xc:none -fill white -stroke black \
          -font Yanone-Kaffeesatz-Regular -pointsize 300 -gravity center \
          -draw "text 0,0 '1'"   img/1.png

### Weißes Bild für Cheese ###

# Test > Erfolg [colorspace vermutlich überflüssig]
#convert -size 320x320 xc:white -depth 16 -colorspace RGB -set colorspace RGB -define png:color-type=6 img/white.png

# Version: rein Weiß
#convert -size 1920x1088 xc:white -define png:color-type=6 img/white.png

# Version: Transparent Weiß
convert -size 1920x1088 xc:white -alpha set -channel Alpha -evaluate set 80% -define png:color-type=6 img/white.png