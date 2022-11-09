import redis
import json
import time
from datetime import datetime
import numpy as np

# Sensors #
from sensors.cpuTemp import CpuTemp
from sensors.lipoCell import LipoCell
from sensors.tempProbe import TempProbe
from sensors.sensorsBoard import Accel, Gyro, Mag

time.sleep(1)

sensors = [
    {"name": "temp_cpu", "script": CpuTemp, "avg": []},
    {"name": "lipo_cell_0", "script": LipoCell(0), "avg": []},
    {"name": "lipo_cell_1", "script": LipoCell(1), "avg": []},
    {"name": "lipo_cell_2", "script": LipoCell(2), "avg": []},
    {"name": "temp_probe_0", "script": TempProbe(3), "avg": []},
    {"name": "accel", "script": Accel, "subs": ["ax", "ay", "az"], "avg_ax": [],"avg_ay": [],"avg_az": []},
    {"name": "gyro", "script": Gyro, "subs": ["wx", "wy", "wz"], "avg_wx": [],"avg_wy": [],"avg_wz": []},
    {"name": "mag", "script": Mag, "subs": ["mx", "my", "mz"], "avg_mx": [],"avg_my": [],"avg_mz": []},
    ]
# ---------

r = redis.Redis(host='localhost', port=6379, db=0) # Initialize Redis connection
data_retention = 360000 # Time in ms before data is deleted, 600000 = 10min

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
    now = int(datetime.utcnow().timestamp()*1e3)
    for sensor in sensors:
        val = sensor["script"].poll()["value"]
        if type(val) is dict:
            for x in val:
                if len(sensor[f'avg_{x}']) >= 10:
                    npArray = np.array(sensor[f'avg_{x}'])
                    average = np.average(npArray)
                    sensor[f'avg_{x}'] = []
                    r.ts().add(f'{sensor["name"]}_{x}', now, average)
                sensor[f'avg_{x}'].append(val[x])
        else:
            if len(sensor["avg"]) >= 10:
                npArray = np.array(sensor["avg"])
                average = np.average(npArray)
                sensor["avg"] = []
                r.ts().add(sensor["name"], now, average)
            sensor["avg"].append(val)

create_time_series()


print("📡  Continous sensor polling started")
starttime = time.time()
while True:
    poll_sensors()
    time.sleep(0.2 - ((time.time() - starttime) % 0.2))
