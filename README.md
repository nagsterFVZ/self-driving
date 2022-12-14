# self-driving

## Setup

``` bash
# Install Python dependencies
sudo pip3 install -r requirements.txt

# Install Linux dependencies
chmod +x packages.bash # Make script executable
sudo ./packages.bash

# Run Server (http://localhost:8080)
flask run

# Run Server on all connections
flask run --host=0.0.0.0


gunicorn --bind 0.0.0.0:8080 wsgi:app
```

## Project Structure Overview
![Project Diagram](https://i.imgur.com/POkYepL.png)


## Sources
|Description|Source|
|---|---|
|MPU9255 Readout|https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer|
|Installing CircuitPython Libraries on Raspberry Pi|https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi|
|NeoPixel|https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage|