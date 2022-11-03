#Import necessary libraries
from flask import Flask, render_template, Response, jsonify
from picamera2 import Picamera2
from libcamera import Transform
import cv2
import time
from gpiozero import CPUTemperature
import redis
from datetime import datetime


r = redis.Redis(host='localhost', port=6379, db=0) # Initialize Redis connection
sensors = [
    {"name": "temp_cpu"},
    {"name": "lipo_cell_0"},
    {"name": "lipo_cell_1"},
    {"name": "lipo_cell_2"},
    {"name": "temp_probe_0"},
    {"name": "accel", "subs": ["ax", "ay", "az"]},
    {"name": "gyro", "subs": ["wx", "wy", "wz"]},
    {"name": "mag", "subs": ["mx", "my", "mz"]},
    ]


# picam2 = Picamera2()
# camera_config = picam2.create_video_configuration(main={"format": 'XRGB8888', "size": (1920, 1080)}, transform=Transform(vflip=0))
# picam2.configure(camera_config)
# picam2.start()
time.sleep(2.0)

app = Flask(__name__)

def gen_frames():  
    while True:
        im = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/temps")
def temps():
    cpu = CPUTemperature()
    return jsonify({'cpu': cpu.temperature})

@app.route("/stats")
def stats():
    response = {}
    now = int(datetime.utcnow().timestamp()*1e3)
    for sensor in sensors:
        if "subs" in sensor:
            for sub in sensor["subs"]:
                response[f'{sensor["name"]}_{sub}'] = r.ts().range(f'{sensor["name"]}_{sub}', now-300000, now)
        else:
            response[f'{sensor["name"]}'] = r.ts().range(f'{sensor["name"]}', now-300000, now)
    return jsonify(response)