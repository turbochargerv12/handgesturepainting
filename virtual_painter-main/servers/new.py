from fastapi import FastAPI, WebSocket
import cv2
import numpy as np
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi_websocket_rpc import WebsocketRPCEndpoint
from io import BytesIO
import cv2
import uvicorn
 
app = FastAPI()
@app.websocket("/video")
async def video_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        nparr = np.fromstring(data.split(",")[1].decode("base64"), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        retval, buf = cv2.imencode(".jpg", gray)
        dataUrl = "data:image/jpeg;base64," + buf.tostring().encode("base64")
        await websocket.send_text(dataUrl)
# Serve Vue.js website
app.mount("/", StaticFiles(directory="c:/Users/angel/Documents/handgesturepainting/Canva/handy/"), name="static")
# WebSocket endpoint for receiving and sending video frames
@app.websocket("/video_stream")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    print("hello")
    while True:
        # Receive video frame from Vue.js website
        frame_data = await websocket.receive_bytes()
        frame_bytes = BytesIO(frame_data).read()
        frame = cv2.imdecode(np.frombuffer(frame_bytes, dtype='uint8'), -1)
        # Perform image processing on the frame
        # ...
        # Send processed frame back to Vue.js website
        _, frame_data = cv2.imencode('.jpg', frame)
        await websocket.send_bytes(frame_data.tobytes())  
# uvicorn.run(app, host="127.0.0.1", port=5000)
# uvicorn new:app --host 127.0.0.1 --port 5000
# import main