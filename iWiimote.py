import requests
import fire
class iWiimote(object):
    def __init__(self, channels):
        self.channels = channels
        ip_addr = fire.Fire(getIpString)
        self.url = "http://"+ip_addr + "/get?" + ("&".join(channels))
    def getData(self):
            data = requests.get(url=self.url).json()
            clean_data = {}
            for channel in self.channels:
                clean_data[channel] = data["buffer"][channel]["buffer"][0]
            return clean_data

# Doesn't do anything but expose the url to fire
def getIpString(ip):
        addr = ip.strip()
        nparts = len(addr.split("."))
        if nparts !=4:
            raise ValueError("Bad Ip String")
        return addr
