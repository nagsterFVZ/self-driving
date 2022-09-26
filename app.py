#Import necessary libraries
from flask import Flask, render_template, Response
from picamera2 import Picamera2
from libcamera import Transform
import cv2
import time
#Initialize the Flask app
app = Flask(__name__)

picam2 = Picamera2()
camera_config = picam2.create_video_configuration(main={"size": (1280, 720)}, transform=Transform(vflip=1))
picam2.configure(camera_config)
picam2.start()
time.sleep(2)
im = picam2.capture_array()

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
