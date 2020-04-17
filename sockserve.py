import asyncio
import websockets
import socket

async def hello(websocket, path):
	while True:
		name = await websocket.recv()
		count = 70
		if name:
			print(f"< {name}")

			greeting = f"Hello {name}!"

			await websocket.send(greeting)
			print(f"> {greeting}")

			if count <= 0:
				break
			count -= 1

ipAddr = socket.gethostbyname(socket.gethostname())
print(ipAddr)
start_server = websockets.serve(hello, ipAddr , 12000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()