#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import ssl
import websockets
import os
import socket
import keyboard
from pynput.mouse import Button, Controller
import json
import mouse

pynput_mouse = Controller()

def parseMessage(msg):
    pass

def startControllerServer(IP):
    async def hello(websocket, path):
        while True:
            message = await websocket.recv()
            decode = json.loads(message)
            if 'gyrX' in decode and 'gyrZ' in decode:
                gyrX = decode['gyrX']
                gyrZ = decode['gyrZ']
                mouse.move(-gyrZ, -gyrX, absolute=False)
                # mouse.move_relative(-gyrZ,-gyrX)

            if 'mouse' in decode:
                command = decode['mouse'].split()
                if command[0] == 'press':
                    if(command[1] == "left"):
                        pynput_mouse.press(Button.left)
                    else:
                        pynput_mouse.press(Button.right)
                elif command[0] == 'release':
                    if(command[1] == "left"):
                        pynput_mouse.release(Button.left)
                    else:
                        pynput_mouse.release(Button.right)
                elif command[0] == "scroll":
                    print("dx: " + command[1], " , dy " + command[2])
            if 'key' in decode:
                command = decode['key'].split()
                if command[0] == 'press':
                    keyboard.press(command[1])
                elif command[0] == 'release':
                    keyboard.release(command[1])


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
