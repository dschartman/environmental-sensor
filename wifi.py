from time import sleep

import network

from config import PASSWORD, SSID
from led import led, led_status

wlan = network.WLAN(network.STA_IF)


@led_status
def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            led.on()
            sleep(0)
            led.off()

        print("network config:", wlan.ifconfig())
        for _ in range(0, 5):
            led.on()
            sleep(1)
            led.off()
            sleep(0.5)
