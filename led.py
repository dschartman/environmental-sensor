from machine import Pin

from config import LED_STATUS

led = Pin("LED", Pin.OUT)


def led_status(func):
    def _wrapper(*args, **kwargs):
        if LED_STATUS:
            led.on()
        data = func(*args, **kwargs)
        led.off()

        return data

    return _wrapper
