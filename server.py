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
        try:
            message = await websocket.recv()
            decode = json.loads(message)
            print(message)

            if 'gyrX' in decode and 'gyrZ' in decode:
                gyrZ = decode['gyrZ']
                gyrX = decode['gyrX']
                mouse.move(-gyrZ*51.2, -gyrX*28.8, absolute=False)

            if 'mouse' in decode:
                click = decode['mouse']
                if(click == "Left Click"):
                    mouse.click(mouse.LEFT)

            if 'key' in decode:
                command = decode['key'].split()
                if command[0] == 'press':
                    keyboard.press(command[1])
                elif command[0] == 'release':
                    keyboard.release(command[1])
        except:
            print("connection lost")
            break

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("iwiimote_server.cer")
ssl_context.load_cert_chain(localhost_pem, keyfile="iwiimote_server.key")
print("Server is running!")

start_server = websockets.serve(hello, "192.168.1.3", 12000, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()