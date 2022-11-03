import ADS1115

class LipoCell:
    ads = ADS1115.ADS1115(address=0x48)
    def __init__(self, channel):
        self.channel = channel
    def poll(self):
        volt = round(((LipoCell.ads.readADCSingleEnded(self.channel)*2.2)/1000), 2)
        res = {"name": f'lipo_cell_{self.channel}', "value": volt}
        return res