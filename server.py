#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import pathlib
import ssl
import websockets
import json
import mouse
import keyboard

async def hello(websocket, path):
    while True:
        message = await websocket.recv()
        decode = json.loads(message)

        if 'gyrX' in decode and 'gyrZ' in decode:
            gyrZ = decode['gyrZ']
            gyrX = decode['gyrX']
            mouse.move(-gyrZ*51.2, -gyrX*28.8, absolute=False)

        if 'mouse' in decode:
            click = decode['mouse']
            if(click == "Left Click"):
                mouse.click(mouse.LEFT)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("iwiimote_server.cer")
ssl_context.load_cert_chain(localhost_pem, keyfile="iwiimote_server.key")
print("Server is running!")

start_server = websockets.serve(hello, "192.168.1.234", 12000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()