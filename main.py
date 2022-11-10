from time import sleep

from influx import send_to_influx
from sample import take_reading
from config import SENSOR_SLEEP_TIME

while True:
    print("collecting sensor information...")
    data = take_reading()

    print("sending to influx...")
    send_to_influx(data)

    print("done...")
    sleep(SENSOR_SLEEP_TIME)
