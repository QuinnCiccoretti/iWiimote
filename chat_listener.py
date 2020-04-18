import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:8000/chat/lobby"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")
        while True:
            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
