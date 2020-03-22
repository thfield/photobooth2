#!/usr/bin/env python3
"""
photobooth program
"""
import sys
import yaml
import os
import datetime
from time import sleep

from picamera import PiCamera
from gpiozero import Button, PWMLED, LED, DigitalOutputDevice

def read_config(filepath):
    """
    read the config from a specified path
    return a dictionary with the config settings
    """
    with open(filepath, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def get_subfolder_name(basepath='./'):
    foldername = datetime.datetime.now().strftime('%Y-%m-%d')
    return os.path.join(basepath,foldername)

def get_base_filename():
    return datetime.datetime.now().strftime('%H%M%S')

config = read_config("./config.yaml")
output_folder = get_subfolder_name(config["SAVE_RAW_IMAGES_FOLDER"])
#TODO: make output_folder if doesn't exist

camera = PiCamera()
# camera.resolution = (config["PHOTO_W"], config["PHOTO_H"])

exit_button = Button(config['EXIT_BUTTON_PIN'])
snap_button = Button(config['CAMERA_BUTTON_PIN'])

leds = {
    "r": LED(21),
    "g": LED(13),
    # "rpwm": PWMLED(13),
    # "gpwm": PWMLED(21),
}

def blink(led, t=0.5):
    leds[led].on()
    sleep(t)
    leds[led].off()

def snap():
    filename = get_base_filename()
    camera.start_preview()
    sleep(2)
    camera.capture(output_folder + '/' + filename + '.jpg')
    camera.stop_preview()

while True:
    if exit_button.is_pressed:
        blink("r")
        print('goodbye')
        sys.exit()
    if snap_button.is_pressed:
        blink("g")
        snap()
