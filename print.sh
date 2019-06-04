#!/bin/bash
#echo -e "photos.app.goo.gl/\\n  bZDEwMb6s9oAiqRz8\\n" > /dev/serial0
#filepath='/home/pi/raspberry_pi_photo_booth/photos'
temp="/tmp"
convert $1\_1.jpg -resize '400x400' -modulate 125% -normalize $temp/1.jpg
convert $1\_2.jpg -resize '400x400' -modulate 125% -normalize $temp/2.jpg
convert $1\_3.jpg -resize '400x400' -modulate 125% -normalize $temp/3.jpg
lp -o fit-to-page $temp/1.jpg
lp -o fit-to-page $temp/2.jpg
lp -o fit-to-page $temp/3.jpg
# lp -o fit-to-page /home/pi/raspberry_pi_photo_booth/assets/heading.png
#lp -o fit-to-page $1\_1.jpg
#lp -o fit-to-page $1\_2.jpg
#lp -o fit-to-page $1\_3.jpg
