#!/usr/bin/env python3
"""
photobooth program
"""
import sys
import yaml
import os
import subprocess
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

def create_folder():
    pass

def print():
    pass

def flash():
    # toggles on or off
    pass

config = read_config("./config.yaml")
output_folder = get_subfolder_name(config["SAVE_RAW_IMAGES_FOLDER"])
#TODO: make output_folder if doesn't exist

camera = PiCamera()
# camera.resolution = (config["PHOTO_W"], config["PHOTO_H"])

go_button = Button(config['BUTTON_MIDDLE'])
left_button = Button(config['BUTTON_LEFT'])
right_button = Button(config['BUTTON_RIGHT'])

leds = {
    "led1": LED(config['BUTTON_LEFT'])
    "led2": LED(config['BUTTON_MIDDLE'])
    "led3": LED(config['BUTTON_RIGHT'])
    "lights": LED(config['LIGHT_RELAY'])
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

def countdownlights():
    blink('one')
    blink('two')
    blink('three')

while True:
    if go_button.is_pressed:
        countdownlights("r")
    if left_button.is_pressed:
        blink("lights")
    if right_button.is_pressed:
        sys.exit()
