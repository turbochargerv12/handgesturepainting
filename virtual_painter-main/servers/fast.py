# from flask import Flask
# from flask_socketio import SocketIO
# import cv2
# import numpy as np

# app = Flask(__name__)
# socketio = SocketIO(app)


# @socketio.on('connect', namespace='/video')
# def connect():
#     print('Client connected')

# @socketio.on('disconnect', namespace='/video')
# def disconnect():
#     print('Client disconnected')

# @socketio.on('message', namespace='/video')
# def receive_chunk(chunk):
#     # Process the video chunk using OpenCV or ffmpeg
#     print(f'Received {len(chunk)} bytes')

#     # Continuously receive chunks from the video stream and process them
#     #while True:
#         # Receive a chunk from the WebSocket connection
        
#         # Code to receive a chunk from WebSocket
#     if chunk:
#         # Call the handle_chunk function to process the chunk
#         handle_chunk(chunk)
#     # else:
#     #     # If there's an error receiving the chunk, break out of the loop
#     #     break






# # Define a callback function to handle video chunks
# def handle_chunk(chunk):
#     # Convert the chunk to a NumPy array
#     nparr = np.frombuffer(chunk, np.uint8)
#     # Decode the array into a video frame
#     frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the grayscale frame
#     cv2.imshow('Gray', gray)
#     cv2.waitKey(1)



# # Close the OpenCV window
# cv2.destroyAllWindows()

# if __name__ == '__main__':
#     app.run(debug=True)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW


app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"