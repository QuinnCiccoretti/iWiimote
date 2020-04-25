#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import ssl
import websockets
import os
import socket
import keyboard
import mouse
import json

def parseMessage(msg):
    pass

def startControllerServer(IP):
    async def hello(websocket, path):
        while True:
            try:
                message = await websocket.recv()
                decode = json.loads(message)

                if 'gyrX' in decode and 'gyrZ' in decode:
                    gyrX = decode['gyrX']
                    gyrZ = decode['gyrZ']
                    mouse.move(-gyrZ, -gyrX, absolute=False)

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
    ssl_context.load_cert_chain(certfile="./certificates/iwiimote_server.cer", keyfile="./certificates/iwiimote_server.key")
    print("Server is running!")

    start_server = websockets.serve(hello, IP, 12000, ssl=ssl_context)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    # TODO: Close server with keyboard interrupt inside of run_forever?

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))   
    hostname =  s.getsockname()[0]
    s.close()
    IP = socket.gethostbyname(hostname)
    startControllerServer(IP)