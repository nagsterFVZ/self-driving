import RPi.GPIO as GPIO
from time import sleep

class ESC:
    GPIO.setmode(GPIO.BCM)
    escPin = 18
    minDuty = 5
    maxDuty = 10
    GPIO.setwarnings(False)
    GPIO.setup(escPin,GPIO.OUT)
    pwm = GPIO.PWM(escPin,50)
    pwm.start(0)

    def cal_phase_1(self):
        ESC.pwm.ChangeDutyCycle(ESC.maxDuty)
        
    def cal_phase_2(self):
        ESC.pwm.ChangeDutyCycle(ESC.minDuty)
        sleep(12)
        ESC.pwm.ChangeDutyCycle(0)
        sleep(2)
        ESC.pwm.ChangeDutyCycle(ESC.minDuty)
        sleep(1)
        ESC.pwm.ChangeDutyCycle(ESC.speedCalc(0))

    def arm(self):
        ESC.pwm.start(0)
        sleep(1)
        ESC.pwm.ChangeDutyCycle(ESC.maxDuty)
        sleep(1)
        ESC.pwm.ChangeDutyCycle(ESC.minDuty)
        sleep(1)
        ESC.control()

    def control(self):
        sleep(1)
        ESC.pwm.ChangeDutyCycle(ESC.speedCalc(20))
        sleep(5)
        ESC.pwm.ChangeDutyCycle(ESC.speedCalc(0))
        ESC.pwm.stop()

    def speedCalc(percent):
        if(percent > 100):
            return 7.5
        if(percent < -100):
            return 7.5
        return ((5/200)*percent)+7.5
    
esc = ESC()
# esc.cal_phase_1()
# input()
# esc.cal_phase_2()
input()
esc.control()