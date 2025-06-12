# modules/device_manager.py

import os
import logging
from modules.logging_handler import setup_logger

logger = setup_logger()

def check_i2c_devices():
    devices = []
    try:
        output = os.popen("i2cdetect -y 1").read()
        for line in output.split("\n")[1:]:
            for part in line.split()[1:]:
                if part != "--":
                    devices.append(part)
        logger.info(f"I2C devices found: {devices}")
    except Exception as e:
        logger.error(f"Error while checking I2C devices: {e}")
    return devices

def is_device_present(address):
    devices = check_i2c_devices()
    return address.lower() in [d.lower() for d in devices]

def has_rtc():
    return is_device_present("68")  # DS3231

def has_ina219():
    return is_device_present("40")  # INA219 (peut varier selon config)

def get_hardware_status():
    return {
        "rtc": has_rtc(),
        "ina219": has_ina219(),
        "i2c_devices": check_i2c_devices()
    }
