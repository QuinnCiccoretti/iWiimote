#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import pathlib
import ssl
import websockets
import os

def parseMessage(msg):
    pass

def startControllerServer(IP):
    async def hello(websocket, path):
        while True:
            try:
                name = await websocket.recv()
                print(f"< {name}")

                greeting = f"Hello {name}!"

                await websocket.send(greeting)
                print(f"> {greeting}")
            except Exception as e:
                print('Error!: ', e)
                break
            except KeyboardInterrupt:
                print("Received exit, exiting")
                break

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # server_cer = pathlib.Path('./certificates').with_name("iwiimote_server.cer")
    # server_key = pathlib.Path('./certificates').with_name("iwiimote_server.key")
    ssl_context.load_cert_chain(certfile="./certificates/iwiimote_server.cer", keyfile="./certificates/iwiimote_server.key")
    print("Server is running!")

    start_server = websockets.serve(hello, IP, 12000, ssl=ssl_context)
    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Received exit, exiting")

if __name__ == '__main__':
    startControllerServer("192.168.1.3")