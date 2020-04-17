import asyncio
import websockets

async def hello(websocket, path):
	while True:
	    name = await websocket.recv()
	    if name:
		    print(f"< {name}")

		    greeting = f"Hello {name}!"

		    await websocket.send(greeting)
		    print(f"> {greeting}")

start_server = websockets.serve(hello, "ws://192.168.1.180", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()