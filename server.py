#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print(f"< {name}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("iwiimote_server.cer")
ssl_context.load_cert_chain(localhost_pem, keyfile="iwiimote_server.key")
print("Server is running!")

start_server = websockets.serve(hello, "192.168.1.234", 12000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()