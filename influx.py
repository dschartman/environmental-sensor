import urequests

import wifi
from config import INFLUX_API_TOKEN, INFLUX_WRITE_URL, SENSOR_LOCATION
from led import led_status

headers = {
    "Accept": "application/json",
    "Connection": "close",
    "Content-type": "text/plain; charset=utf-8",
    "Authorization": f"Token {INFLUX_API_TOKEN}",
}


@led_status
def send_to_influx(sensor_data):
    wifi.do_connect()

    fields = (
        "sensors,",
        "location={location}".format(location=SENSOR_LOCATION),
        " ",
        "temperature={temp}".format(temp=sensor_data["temperature"]),
        ",humidity={humidity}".format(humidity=sensor_data["humidity"]),
        ",pressure={pressure}".format(pressure=sensor_data["pressure"]),
        ",gas={gas}".format(gas=sensor_data["gas"]),
    )
    point = "".join(fields)
    resp = urequests.post(INFLUX_WRITE_URL, headers=headers, data=point)
    resp.close()

    print(resp.status_code)
