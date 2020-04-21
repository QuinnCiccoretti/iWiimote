import requests
import fire
class iWiimote(object):
    def __init__(self, ip_addr, channels):
        self.channels = channels
        self.url = "http://"+ip_addr + "/get?" + ("&".join(channels))
    def getData(self):
            data = requests.get(url=self.url).json()
            clean_data = {}
            for channel in self.channels:
                clean_data[channel] = data["buffer"][channel]["buffer"][0]
            return clean_data

    # Doesn't do anything but expose the url to fire
    def getIpString(ip):
        return ip
