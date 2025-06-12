# modules/gpio_control.py

import RPi.GPIO as GPIO
import time

# Mode de numérotation BCM
GPIO.setmode(GPIO.BCM)

# Désactive les avertissements
GPIO.setwarnings(False)

def setup_output(pin):
    GPIO.setup(pin, GPIO.OUT)

def setup_input(pin, pull_up_down=GPIO.PUD_DOWN):
    GPIO.setup(pin, GPIO.IN, pull_up_down=pull_up_down)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)

def toggle(pin):
    GPIO.output(pin, not GPIO.input(pin))

def read_input(pin):
    return GPIO.input(pin)

def cleanup():
    GPIO.cleanup()
