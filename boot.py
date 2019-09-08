import dht
import esp
import gc
import network
import time

from machine import Pin
from umqtt.simple import MQTTClient

import device
import config


gc.enable()
# esp.osdebug(None)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while not wlan.isconnected():
    wlan.connect(config.WIFI_NAME, config.WIFI_PASSWORD)
    time.sleep(1)

    count = 0
    while not wlan.isconnected() and count < 10:
        count += 1
        time.sleep(1)

client = MQTTClient(device.ID, config.SERVER, config.PORT)
client.connect()

sensor = dht.DHT11(Pin(config.PIN))
