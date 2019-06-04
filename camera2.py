#!/usr/bin/env python
"""
photobooth program
"""
import datetime
import yaml
from gpiozero import Button, PWMLED, DigitalOutputDevice

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

def get_subfolder_name(basepath='.'):
    foldername = datetime.datetime.now().strftime('%Y-%m-%d')
    return f"{basepath}/{foldername}"

def get_base_filename():
    return datetime.datetime.now().strftime('%H%M%S')

config = read_config("./config.yaml")

today = get_subfolder_name()
print(today)
