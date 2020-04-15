from aiohttp import ClientSession
import asyncio
import pyautogui


#phyphox configuration
PP_ADDRESS = "http://192.168.1.232"
PP_CHANNELS = ["accX", "accY", "accZ"]

async def fetchJSON(url, session):
	async with session.get(url) as response:
		data = await response.json()
		accX = data["buffer"][PP_CHANNELS[0]]["buffer"][0]
		accY = data["buffer"][PP_CHANNELS[1]]["buffer"][0]
		accZ = data["buffer"][PP_CHANNELS[2]]["buffer"][0]
		# 
		pyautogui.move(-accX*20, accY*20)


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
	N_REQUESTS = 2
	while True:
		future = asyncio.ensure_future(sendNRequests(url, N_REQUESTS))
		loop.run_until_complete(future)
		

if __name__ == '__main__':
	main()
