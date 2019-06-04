from gpiozero import PWMLED, Button
from time import sleep

button1 = Button(16)
button2 = Button(26)

light = PWMLED(13)

light.on()
sleep(1)
light.off()

# leds = {
#     "r": LED(9),
#     "g": LED(11),
#     "b": LED(13),
#     "y": LED(19),
#     "w": LED(26),
# }
#
# def blink(led, t=0.5):
#     leds[led].on()
#     sleep(t)
#     leds[led].off()
# while True:
#     if button1.is_pressed:
#         blink("r")
#     if button2.is_pressed:
#         blink("g")
