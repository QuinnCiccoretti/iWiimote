import asyncio
import websockets
import pathlib
import ssl
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

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("snakeoil.pem")
ssl_context.load_cert_chain(localhost_pem)

ipAddr = socket.gethostbyname(socket.gethostname())
print(ipAddr)
# start_server = websockets.serve(hello, "192.168.1.3" , 12000)
start_server = websockets.serve(
    hello, "192.168.1.3", 12000, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()