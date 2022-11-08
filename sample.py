from machine import I2C, Pin

from bme680 import *
from config import TEMP_OFFSET
from led import led_status

i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
bme = BME680_I2C(i2c=i2c)
led = Pin("LED", Pin.OUT)


def _celcius_to_fahrenheit(temp):
    return temp * 1.8 + 32


@led_status
def take_reading():
    temp = bme.temperature
    return {
        "temperature": _celcius_to_fahrenheit(temp + TEMP_OFFSET),
        "temperature_c": temp + TEMP_OFFSET,
        "humidity": bme.humidity,
        "pressure": bme.pressure,
        "gas": bme.gas,
    }


def print_reading():
    reading = take_reading()
    temperature = str(round(reading["temperature"], 1)) + " F"
    humidity = str(round(reading["humidity"], 2)) + " %"
    pressure = str(round(reading["pressure"], 2)) + " hPa"
    gas = str(round(reading["gas"] / 1000, 2)) + " KOhms"
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Pressure:", pressure)
    print("Gas:", gas)
