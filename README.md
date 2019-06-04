# Raspberry Pi Photo Booth 2
Borrows heavily from https://github.com/jibbius/raspberry_pi_photo_booth

printer drivers: https://github.com/klirichek/zj-58

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
