# Setting up Circuit Python Blinka
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
cd ~
pip3 install --upgrade adafruit-python-shell
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
python3 raspi-blinka.py
pip3 install adafruit-circuitpython-pca9685
pip3 install adafruit-circuitpython-servokit