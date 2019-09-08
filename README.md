# sensor2graph-micropython-esp32

This project shows how to get data from a sensor, save it into a database, and visualize it.

To do that it uses different components. 
A [DHT11](https://learn.adafruit.com/dht) is used as sensor, which can output temperature and humidity as data.
An [ESP32](https://www.espressif.com/en/products/hardware/esp32/overview) reads this data and sends it over WIFI to a MQTT server.
The MQTT server ([Eclipse Mosquitto](https://mosquitto.org/)) serves as an intermediary to receive sensor data and redistribute further.
[Node-RED](https://nodered.org/) gets the data from the MQTT server and saves it into the database.
[PostgreSQL](https://postgresql.org/) is the database that saves the data and allows it to be displayed later.
The visualization is done with [Grafana](https://grafana.com/).

## Setup

### ESP32

#### Wiring

#### Code

> Note: The ESP32 needs to be prepared to run Micropython code. See [https://github.com/danielwohlgemuth/setup-micropython-esp32](https://github.com/danielwohlgemuth/setup-micropython-esp32) on how to do this.

Make a copy of `config.py.example` and rename it to `config.py`. On Linux you can do this with `cp config.py.example config.py`

Set the variables inside `config.py` to the appropriate values for your use. Mainly `WIFI_NAME`, `WIFI_PASSWORD`, and `SERVER`. `SERVER` should be the IP address or DNS name of your MQTT server. On Linux you can find the IP address with `ip a` and look for line that starts with `inet`.

Generate a UUID for every ESP32 you add. You can use `python generate-id.py` to generate the file `device.py` which will contain the new UUID.

Next, copy the necessary files to the ESP32. 

[Ampy](https://github.com/pycampers/ampy) is used to copy the files. [Pipenv](https://docs.pipenv.org/en/latest/) is used as a virtual environment in which ampy is installed. If you have Pipenv installed, run `pipenv install` to install it and be able to use the following commands.

```bash
pipenv run ampy --port /dev/ttyUSB0 put boot.py
pipenv run ampy --port /dev/ttyUSB0 put main.py
pipenv run ampy --port /dev/ttyUSB0 put config.py
pipenv run ampy --port /dev/ttyUSB0 put device.py
```

### Start Mosquitto, Node-RED, PostgreSQL, and Grafana

```bash
sudo docker-compose up -d
```

### Setup Node-RED

Import flow into Node-RED

### Setup PostgreSQL

Click on the inputs to create the tables.

### Setup Grafana

Import dashboard into Grafana


setup docker

start docker-compose

import flow

import dashboard

setup esp32


pipenv run ampy --port /dev/ttyUSB0 ls
pipenv run ampy --port /dev/ttyUSB0 get error.log

pipenv run rshell --port /dev/ttyUSB0 repl

node-red-contrib-postgres-multi


python generate-id.py

## Tips

## Connect to Postgres and inspect the data

```bash
psql -h 192.168.88.247 -U postgres -d postgres
```

```sql
SELECT * FROM sensor;
SELECT * FROM device;
```

### Setup logging

```python
import time


def log(msg):
    localtime = time.localtime()
    file = open('error.log', 'a')
    file.write(str(localtime) + ': ' + msg + '\n')
    file.close()

log('esp')
```

### Read logs

```bash
pipenv run ampy --port /dev/ttyUSB0 ls
pipenv run ampy --port /dev/ttyUSB0 get error.log
```

```bash
pipenv run rshell --port /dev/ttyUSB0 repl
```

```python
f = open('error.log', 'f')
print(f.read())
f.close()
```
