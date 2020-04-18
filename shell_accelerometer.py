from aiohttp import ClientSession
import asyncio
import keyboard
import mouse
from controls import Game


#phyphox configuration
PP_ADDRESS = "http://192.168.1.4"
PP_CHANNELS = ["accX", "accY", "accZ"]

async def fetchJSON(url, session):
	async with session.get(url) as response:
		data = await response.json()
		accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
		accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
		accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
		# 
		mouse.move(accY*10,0, absolute=False)
		if(accX and accY and accZ):
			print(accX, accY, accZ, sep=" ")
			if(accY < -2.0):
				keyboard.press('left')
			else:
				keyboard.release('left')

			if(accY > 2.5):
				keyboard.press('right')
			else:
				keyboard.release('right')

			if(accZ < -1):
				keyboard.press('up')
			else:
				keyboard.release('up')


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
