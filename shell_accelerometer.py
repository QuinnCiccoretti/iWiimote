from aiohttp import ClientSession
import asyncio
import pyautogui


#phyphox configuration
PP_ADDRESS = "http://192.168.1.232"
PP_CHANNELS = ["accX", "accY", "accZ"]

async def pollSensor(url):
	async with ClientSession() as session:
		async with session.get(url) as response:
			data = await response.json()
			accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
			accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
			accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
			# 
			pyautogui.move(-accX*20, accY*20)

def main():
	loop = asyncio.get_event_loop()
	url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))

	while True:
		task = asyncio.ensure_future(pollSensor(url))
		loop.run_until_complete(task)
		

if __name__ == '__main__':
	main()