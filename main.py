import machine
import ntptime
import time
import ujson

import device
import config


ntptime.settime()
localtime = time.localtime()

#  '2007-03-01T13:00:00Z'
localtime_formated = '{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z'.format(
    localtime[0], localtime[1], localtime[2], localtime[3], localtime[4], localtime[5])

sensor.measure()

measure = {
    "device": device.ID,
    "datetime": localtime_formated,
    "temperature": sensor.temperature(),
    "humidity": sensor.humidity()
}
msg = ujson.dumps(measure)

client.publish(config.TOPIC, msg)

time.sleep(1)

machine.deepsleep(config.DEEPSLEEP_TIME_MS)
