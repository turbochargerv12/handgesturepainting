from typing import Set
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="public"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)


# Set to store all connected clients
clients: Set[WebSocket] = set()

# WebSocket endpoint that will broadcast messages to all connected clients
@app.websocket("/video")
async def video(websocket: WebSocket):
    # Accept the WebSocket connection
    await websocket.accept()

    # Add the WebSocket client to the set of connected clients
    clients.add(websocket)

    try:
        while True:
            # Receive a message from the client
            message = await websocket.receive()

            # If the message is a string, ignore it (we're only interested in binary data)
            if isinstance(message, str):
                continue

            # Otherwise, the message is a binary blob representing a video chunk
            # Send it to all connected clients
            await broadcast(message)

    finally:
        # Remove the WebSocket client from the set of connected clients
        clients.remove(websocket)

# Function that broadcasts a message to all connected clients
async def broadcast(message):
    for client in clients:
        await client.send_bytes(message)

# Route that serves an HTML page with a JavaScript script that connects to the WebSocket endpoint
@app.get("/")
async def index():
    return HTMLResponse("""
        <html>
            <head>
                <title>Real-time Video Streaming</title>
            </head>
            <body>
                <video id="video" autoplay></video>
                <script>
                    const video = document.getElementById("video");
                    const ws = new WebSocket(`ws://localhost:8000/video`);
                    let mediaRecorder = null;
                    let recordedChunks = [];

                    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
                        video.srcObject = stream;

                        mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });

                        mediaRecorder.ondataavailable = (event) => {
                            if (event.data && event.data.size > 0) {
                                recordedChunks.push(event.data);
                                ws.send(event.data);
                            }
                        }

                        mediaRecorder.start(100);
                    }).catch((error) => {
                        console.error(error);
                    });

                    ws.onmessage = (event) => {
                        const data = event.data;
                        if (data instanceof Blob) {
                            const url = URL.createObjectURL(data);
                            video.src = url;
                        }
                    };
                </script>
            </body>
        </html>
    """)
