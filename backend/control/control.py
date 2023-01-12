# """Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
# import time
# from adafruit_servokit import ServoKit

# # Set channels to the number of servo channels on your kit.
# # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
# kit = ServoKit(channels=16)

# # kit.servo[1].angle = 180
# # kit.servo[1].angle = 0

# kit.continuous_servo[0].throttle = 1
# input("Sending High Throttle, press enter after hearing beep-beep")
# kit.continuous_servo[0].throttle = 0
# input("Sending Low Throttle, press enter after the long beep")

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 46

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
#max 6553; min 3276; mid 4915; off 0
pca.channels[0].duty_cycle = 4915
input('wait')
pca.channels[0].duty_cycle = 3276
input('wait')
# pca.channels[0].duty_cycle = 0x2000
# input('wait')