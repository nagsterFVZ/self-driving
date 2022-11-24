from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from time import sleep

class Esc:
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 46
    pwm = pca.channels[0]
    minDuty = 3276
    maxDuty = 6553
    midDuty = 4915

    def test():
        return True

    def cal_phase_1():
        Esc.pwm.duty_cycle = Esc.maxDuty
        return True
        
    def cal_phase_2():
        Esc.pwm.duty_cycle = Esc.minDuty
        sleep(12)
        Esc.pwm.duty_cycle = 0
        sleep(2)
        Esc.pwm.duty_cycle = Esc.minDuty
        sleep(2)
        Esc.pwm.duty_cycle = Esc.midDuty
        return True

    def arm():
        Esc.pwm.duty_cycle = 0
        sleep(1)
        Esc.pwm.duty_cycle = Esc.midDuty
        sleep(1)
        # Esc.pwm.duty_cycle = 0)
        return True

    def control(speed):
        Esc.pwm.duty_cycle = Esc.speedCalc(speed)
        return True

    #max 6553; min 3276;
    def speedCalc(percent):
        if(percent > 100):
            return 7.5
        if(percent < -100):
            return 7.5
        return ((5/200)*percent)+7.5