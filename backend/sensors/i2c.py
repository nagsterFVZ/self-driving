from mpu9255_i2c import *
import ADS1115
import numpy
ads = ADS1115.ADS1115(address=0x48)

def tempProbes():
    mVolt = ads.readADCSingleEnded(3)
    temp = numpy.log((1.18467/(mVolt/1000))-0.3899)/-0.040978
    print("{:.0f} degrees celcius".format(temp))


while 1:
    # tempProbes()
    volt = ads.readADCSingleEnded(0)*2.2
    print(volt)
    time.sleep(1)    

# time.sleep(1) # delay necessary to allow mpu9250 to settle

# print('recording data')
# while 1:
#     try:
#         ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
#         mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
#     except:
#         continue
    
#     print('{}'.format('-'*30))
#     print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az))
#     print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(wx,wy,wz))
#     print('mag [uT]:   x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(mx,my,mz))
#     print('{}'.format('-'*30))
#     time.sleep(1)