if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
apt update  # To get the latest package lists
apt install -y python3-picamera2
apt install -y python3-pyqt5 python3-opengl
apt install -y python3-opencv
apt install -y opencv-data
apt install -y python-smbus
apt install -y i2c-tools