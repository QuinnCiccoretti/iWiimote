import requests
import fire
class iWiimote(object):
    def __init__(self, channels):
        self.channels = channels
        args = fire.Fire(getIpString)
        ip_addr = args[0]
        self.iOS = args[1]
        #inconsistent naming across phone os
        if(self.iOS):
            modified_c = []
            for channel in self.channels:
                modified_c.append(channel.replace("gyr", "gyro"))
            self.channels = modified_c
        print(self.channels)
        self.url = "http://"+ip_addr + "/get?" + ("&".join(self.channels))
    def getData(self):
            data = requests.get(url=self.url).json()
            clean_data = {}
            for channel in self.channels:
                key = channel
                #inconsistent naming across phone os
                if(self.iOS):
                    key = key.replace("gyro", "gyr")
                clean_data[key] = data["buffer"][channel]["buffer"][0]
            return clean_data

# Doesn't do anything but expose the url to fire
def getIpString(ip, iOS=False):
        addr = ip.strip()
        nparts = len(addr.split("."))
        if nparts !=4:
            raise ValueError("Bad Ip String")
        return [addr, iOS]
