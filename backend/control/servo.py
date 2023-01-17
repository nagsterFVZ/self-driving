from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from time import sleep

class Servo:
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 46
    pwm = pca.channels[1]
    angle = 0
    minDuty = 3276
    maxDuty = 6553
    midDuty = 4915

    def set(angle):
        Servo.pwm.duty_cycle = Servo.angleCalc(angle)
        return True
    
    def increment(modifier):
        Servo.angle = Servo.angle + modifier
        Servo.pwm.duty_cycle = Servo.angleCalc(Servo.angle)
        return True
    
    def angleCalc(angle):
        if(angle > 90):
            return int(1639 / 90 * 90 + 4915)
        if(angle < -90):
            return int(1639 / 90 * -90 + 4915)
        return int(1639 / 90 * angle + 4915)