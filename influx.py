import urequests
from config import INFLUX_API_TOKEN, LOCATION, INFLUX_WRITE_URL
import wifi
from led import led_status


headers = {
    'Accept': 'application/json',
    'Connection': 'close',
    'Content-type': 'text/plain; charset=utf-8',
    'Authorization': f"Token {INFLUX_API_TOKEN}"
}

@led_status
def send_to_influx(sensor_data):
    wifi.do_connect()
    
    fields = (
        u'sensors,',
        u'location={location}'.format(location=LOCATION),
        u' ',
        u'temperature={temp}'.format(temp=sensor_data['temperature']),
        u',humidity={humidity}'.format(humidity=sensor_data['humidity']),
        u',pressure={pressure}'.format(pressure=sensor_data['pressure']),
        u',gas={gas}'.format(gas=sensor_data['gas'])
    )
    point = ''.join(fields)
    resp = urequests.post(INFLUX_WRITE_URL, headers=headers, data=point)
    resp.close()

