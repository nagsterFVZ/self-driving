from sensors.mpu9255_i2c import *

class Accel:
    def poll():
        val = mpu6050_conv_accel()
        return val

class Gyro:
    def poll():
        val = mpu6050_conv_gyro()
        return val

class Mag:
    def poll():
        val = AK8963_conv()
        return val