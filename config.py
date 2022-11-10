import ujson


with open("config.json") as data_file:
    _config = ujson.load(data_file)


WIFI_SSID = _config["WIFI_SSID"]
WIFI_PASSWORD = _config["WIFI_PASSWORD"]

SENSOR_LED_STATUS = _config["SENSOR_LED_STATUS"]
SENSOR_LOCATION = _config["SENSOR_LOCATION"]
SENSOR_TEMP_OFFSET = _config["SENSOR_TEMP_OFFSET"]
SENSOR_SLEEP_TIME = _config.get("SENSOR_SLEEP_TIME", 60)

INFLUX_URL = _config["INFLUX_URL"]
INFLUX_API_TOKEN = _config["INFLUX_API_TOKEN"]
INFLUX_ORG = _config["INFLUX_ORG"]
INFLUX_BUCKET = _config["INFLUX_BUCKET"]
INFLUX_WRITE_URL = (
    f"{INFLUX_URL}/api/v2/write?org={INFLUX_ORG}&bucket={INFLUX_BUCKET}&precision=ns"
)
