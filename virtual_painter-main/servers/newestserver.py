import asyncio
import websockets

async def handle_video(websocket, path):
    # Open a new file to write incoming video chunks
    with open('received_video.webm', 'wb') as f:
        async for data in websocket:
            # Write the chunk to the file
            f.write(data)

async def main():
    async with websockets.serve(handle_video, 'localhost', 5000):
        await asyncio.Future()  # Run the server indefinitely

if __name__ == '__main__':
    asyncio.run(main())
