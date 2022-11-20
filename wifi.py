from time import sleep

from config import WIFI_PASSWORD, WIFI_SSID
from led import led, led_status


@led_status
def do_connect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            led.on()
            sleep(0)
            led.off()

        print("network config:", sta_if.ifconfig())
        for _ in range(0, 5):
            led.on()
            sleep(1)
            led.off()
            sleep(0.5)
