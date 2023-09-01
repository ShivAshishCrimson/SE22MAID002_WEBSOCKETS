#SE22MAID002 SERVER ASSIGNMENT 1 
import asyncio
from websockets.server import serve

async def serverResponse(websocket):
    async for msg in websocket:
        print(f"Server Received: {msg}")
        res = "Server Says Hello"
        await websocket.send(res)
        print("Server Sent: {res}")

async def main():
    async with serve(serverResponse, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())