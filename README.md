# Raspberry Pi Photo Booth 2
Borrows heavily from https://github.com/jibbius/raspberry_pi_photo_booth

printer setup: https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/connect-and-configure-printer

program startup
  read config
  set config object
idle loop/watch for button press
  change overlay
photo loop
  show countdown
  turn on flash
  take & save photo
  turn off flash
  save photos elsewhere
  print photos

config objects
  - button pin
  - exit button pin
  - flash relay pin
  - number of copies to print copies
  - display resolution
  - image save destination
  - image capture size
  - image rotation
