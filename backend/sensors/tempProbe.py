import ADS1115
import numpy

class TempProbe:
    ads = ADS1115.ADS1115(address=0x49)
    def __init__(self, channel):
        self.channel = channel
    def poll(self):
        mVolt = TempProbe.ads.readADCSingleEnded(self.channel)
        temp = numpy.log((1.18467/(mVolt/1000))-0.3899)/-0.040978
        res = {"name": f'temp_probe_{self.channel}', "value": temp}
        return res