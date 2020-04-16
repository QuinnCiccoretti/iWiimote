import requests
import pyautogui

import asyncio
import aiohttp
from aiohttp import ClientSession

#phyphox configuration
# https://phyphox.org/remote-control/
PP_ADDRESS = "http://192.168.1.4"
PP_CHANNELS = ["accX", "accY", "accZ", "gyrX", "gyrY", "gyrZ"]
sampling_rate = 100

url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))

#animation and data collection config
PREV_SAMPLE = 50
INTERVALS = 1000/sampling_rate


#global var to save timestamp
xs = []


# make one of them true at a time
isAnimate = False
isCollectData = True

async def getSensorData():
    async with ClientSession() as session:
        async with session.get(url) as response:
            # Arrays to store data
            accelerometer = []
            accelerometer_w_g = []
            gyroscope = []
            magnetometer = []
            
            data = await response.json()
            accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
            accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
            accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
            print (accX, ' ', accY, ' ', accY)
            # return [accX, accY, accZ]
    
    
def main():        
    if isCollectData == True:
        loop = asyncio.get_event_loop()
        loop.run_forever()
    #    while True:
    #        getSensorData()
        #   [t, naccX, naccY, naccZ] = getData()
        # #   print(t, ' ', naccX, ' ', naccY, ' ', naccZ)
        #   if (False and naccX and naccY):
        #     pyautogui.move(-1*naccX*10, naccY*10)
          #time.sleep(INTERVALS/1000)   # Delays for INTERVALS seconds.

if __name__ == '__main__':
    main()





# %%
