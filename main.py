from time import sleep
from sample import take_reading
from influx import send_to_influx


while True:
    print('collecting sensor information...')
    data = take_reading()
    
    print('sending to influx...')
    send_to_influx(data)
    
    print('done...')
    sleep(60)