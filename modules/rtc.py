import datetime

try:
    import board
    import busio
    import adafruit_ds3231

    i2c = busio.I2C(board.SCL, board.SDA)
    rtc = adafruit_ds3231.DS3231(i2c)
    rtc_available = True

except Exception:
    rtc_available = False

def get_current_time():
    """Retourne l'heure actuelle depuis le module RTC ou le système si indisponible."""
    if rtc_available:
        try:
            return rtc.datetime
        except Exception:
            pass
    return datetime.datetime.now()
