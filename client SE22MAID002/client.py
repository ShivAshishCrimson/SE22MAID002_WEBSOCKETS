#SE22MAID002 CLIENT ASSIGNMENT 1 
import asyncio
from websockets.sync.client import connect as handshake

def sendMessage(msg):
    with handshake("ws://localhost:8765") as websocket:
        websocket.send(msg)
        print(f"Client Sent: {msg}")
        severResponse = websocket.recv()
        print(f"Client Received: {severResponse}")
sendMessage("Client Says Hello")