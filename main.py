import time
time.sleep(1)

import dht
import esp
import gc
import machine
import network
import ujson

from machine import Pin
from umqtt.simple import MQTTClient

import config


gc.enable()
# esp.osdebug(None)

sensor = dht.DHT11(Pin(config.PIN))
sensor.measure()

measure = {
    "device": config.DEVICE_NAME,
    "temperature": sensor.temperature(),
    "humidity": sensor.humidity()
}
msg = ujson.dumps(measure)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while not wlan.isconnected():
    wlan.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    time.sleep(1)

    count = 0
    while not wlan.isconnected() and count < 10:
        count += 1
        time.sleep(1)

client = MQTTClient(config.DEVICE_NAME, config.SERVER, config.PORT)
client.connect()

client.publish(config.TOPIC, msg)

time.sleep(1)

machine.deepsleep(config.DEEPSLEEP_TIME_MS)
