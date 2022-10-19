import redis
import json
import time

# Sensors #
from sensors.cpuTemp import CpuTemp
from sensors.lipoCell import LipoCell
from sensors.tempProbe import TempProbe
from sensors.sensorsBoard import Accel, Gyro, Mag

time.sleep(1)

sensors = [
    {"name": "temp_cpu", "script": CpuTemp},
    {"name": "lipo_cell_0", "script": LipoCell(0)},
    {"name": "lipo_cell_1", "script": LipoCell(1)},
    {"name": "lipo_cell_2", "script": LipoCell(2)},
    {"name": "temp_probe_0", "script": TempProbe(3)},
    {"name": "accel", "script": Accel, "subs": ["ax", "ay", "az"]},
    {"name": "gyro", "script": Gyro, "subs": ["wx", "wy", "wz"]},
    {"name": "mag", "script": Mag, "subs": ["mx", "my", "mz"]},
    ]
# ---------

r = redis.Redis(host='localhost', port=6379, db=0) # Initialize Redis connection
data_retention = 600000 # Time in ms before data is deleted, 600000 = 10min

def create_time_series():
    print("⏱  Creating Time Series")
    for sensor in sensors:
        if "subs" in sensor:
            for sub in sensor["subs"]:
                if r.exists(f'{sensor["name"]}_{sub}'):
                    print("     🟠 " + f'{sensor["name"]}_{sub}')
                else:
                    r.ts().create(f'{sensor["name"]}_{sub}', retension_msecs=data_retention)
                    print("     🟢 " + f'{sensor["name"]}_{sub}')
        else:
            if r.exists(sensor["name"]):
                print("     🟠 " + sensor["name"])
            else:
                r.ts().create(sensor["name"], retension_msecs=data_retention)
                print("     🟢 " + sensor["name"])

def poll_sensors():
    for sensor in sensors:
        val = sensor["script"].poll()["value"]
        if type(val) is dict:
            for x in val:
                r.ts().add(f'{sensor["name"]}_{x}', "*", val[x])
        else:
            r.ts().add(sensor["name"], "*", val)

create_time_series()


print("📡  Continous sensor polling started")
starttime = time.time()
while True:
    poll_sensors()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))