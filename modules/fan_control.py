import RPi.GPIO as GPIO
import time
import os

# Configuration
FAN_PIN = 18  # GPIO utilisé pour le ventilateur
TEMP_THRESHOLD = 55  # Température en °C pour déclencher le ventilateur

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, GPIO.LOW)

def get_cpu_temp():
    """
    Lit la température actuelle du CPU.
    """
    try:
        output = os.popen("vcgencmd measure_temp").readline()
        temp_str = output.replace("temp=", "").replace("'C\n", "")
        return float(temp_str)
    except:
        return 0.0

def control_fan():
    """
    Active ou désactive le ventilateur selon la température du CPU.
    """
    temp = get_cpu_temp()
    if temp >= TEMP_THRESHOLD:
        GPIO.output(FAN_PIN, GPIO.HIGH)
        print(f"[SPYNBOOX] Ventilateur ON - {temp:.1f}°C")
    else:
        GPIO.output(FAN_PIN, GPIO.LOW)
        print(f"[SPYNBOOX] Ventilateur OFF - {temp:.1f}°C")

def cleanup():
    """
    Nettoie les broches GPIO avant la sortie.
    """
    GPIO.output(FAN_PIN, GPIO.LOW)
    GPIO.cleanup()
