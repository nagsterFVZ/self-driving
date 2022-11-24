#Import necessary libraries
from flask import Flask, render_template, Response, jsonify, request
from picamera2 import Picamera2
from libcamera import Transform
import cv2
import time
from gpiozero import CPUTemperature
import redis
from datetime import datetime

#Custom Scripts
from control.esc import Esc


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


picam2 = Picamera2()
camera_config = picam2.create_video_configuration(main={"format": 'XRGB8888', "size": (1920, 1080)}, transform=Transform(vflip=0))
picam2.configure(camera_config)
picam2.start()
time.sleep(2.0)

app = Flask(__name__)

def gen_frames():  
    while True:
        im = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/api')
def index():
    return render_template('index.html')

@app.route('/api/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/api/temps")
def temps():
    cpu = CPUTemperature()
    return jsonify({'cpu': cpu.temperature})

@app.route("/api/stats")
def stats():
    data = {}
    now = int(datetime.utcnow().timestamp()*1e3)
    for sensor in sensors:
        if "subs" in sensor:
            for sub in sensor["subs"]:
                data[f'{sensor["name"]}_{sub}'] = r.ts().range(f'{sensor["name"]}_{sub}', now-300000, now)
        else:
            data[f'{sensor["name"]}'] = r.ts().range(f'{sensor["name"]}', now-300000, now)
    return jsonify(data)

@app.route("/api/esc/test")
def esc_test():
    working = Esc.test()
    return jsonify({'working': working})

@app.route("/api/esc/cal/1")
def esc_cal_1():
    complete = Esc.cal_phase_1()
    return jsonify({'complete': complete, "message": "Calibration Phase 1"})

@app.route("/api/esc/cal/2")
def esc_cal_2():
    complete = Esc.cal_phase_2()
    return jsonify({'complete': complete, "message": "Calibration Phase 2"})

@app.route("/api/esc/arm")
def esc_arm():
    complete = Esc.arm()
    return jsonify({'complete': complete, "message": "Armed"})

@app.route("/api/esc/control")
def esc_control():
    speed = request.args.get('speed')
    complete = Esc.control(int(speed))
    return jsonify({'complete': complete, "message": f'Speed run at {speed}'})

if __name__ == "__main__":
    app.run()
