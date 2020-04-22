from aiohttp import ClientSession
import asyncio
import keyboard
import mouse
from controls import Game


#phyphox configuration
PP_ADDRESS = "http://192.168.1.4"
PP_CHANNELS = ["accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ"]
# PP_CHANNELS = ["accX", "accY", "accZ", "gyrX", "gyrY", "gyrZ"]

async def fetchJSON(url, session):
	async with session.get(url) as response:
		data = await response.json()
		# Accelerometer
		accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
		accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
		accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
		# Gyroscope
		gyrX = data["buffer"][PP_CHANNELS[3]]["buffer"][0]
		gyrY = data["buffer"][PP_CHANNELS[4]]["buffer"][0]
		gyrZ = data["buffer"][PP_CHANNELS[5]]["buffer"][0]

		# 
		if(accX and accY and accZ):
			# print(gyrX, gyrY, gyrZ, sep=" ")
			mouse.move(-gyrZ*20, -gyrX*20, absolute=False)
			# print(mouse.get_position())
			# if accY > 0.75 or accY < -0.75:
			# 	mouse.move(accY*5, 0, absolute=False)

			# if(accZ < -1):
			# 	keyboard.press('space')
			# else:
			# 	keyboard.release('space')

			# if(accX < -1):
			# 	mouse.press(mouse.LEFT)
			# 	mouse.release(mouse.LEFT)


async def sendNRequests(url, n):
	tasks = []

	# Fetch all responses within one Client session,
	# keep connection alive for all requests.
	async with ClientSession() as session:
		for i in range(n):
			task = asyncio.ensure_future(fetchJSON(url, session))
			tasks.append(task)
		await asyncio.gather(*tasks)

			
def main():
	loop = asyncio.get_event_loop()
	url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))
	N_REQUESTS = 1
	while True:
		future = asyncio.ensure_future(sendNRequests(url, N_REQUESTS))
		loop.run_until_complete(future)
		

if __name__ == '__main__':
	main()
