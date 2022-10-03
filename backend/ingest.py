import redis
import json
import time

# Sensors #
from sensors.cpuTemp import CpuTemp

sensors = [{"name": "temp_cpu", "script": CpuTemp}]
# ---------

r = redis.Redis(host='localhost', port=6379, db=0) # Initialize Redis connection
data_retention = 600000 # Time in ms before data is deleted, 600000 = 10min

def create_time_series():
    print("⏱  Creating Time Series")
    for sensor in sensors:
        if r.exists(sensor["name"]):
            print("     🟠 " + sensor["name"])
        else:
            r.ts().create(sensor["name"], retension_msecs=data_retention)
            print("     🟢 " + sensor["name"])

def poll_sensors():
    for sensor in sensors:
        r.ts().add(sensor["name"], "*", sensor["script"].poll())

create_time_series()


print("📡  Continous sensor polling started")
starttime = time.time()
while True:
    poll_sensors()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))