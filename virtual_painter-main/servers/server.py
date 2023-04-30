
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
# from main import framework

import numpy as np
from PIL import Image
from io import BytesIO
import cv2   
import io
import base64
from PIL import UnidentifiedImageError
import PIL
from pathlib import Path



app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def home():
    return 'succesful'

@app.route('/image', methods=['POST'])
@cross_origin(supports_credentials=True)
def process_image():
    chunk = request.get_data() 
    print(f'Received {len(chunk)} bytes')

    # Continuously receive chunks from the video stream and process them
    #while True:
        # Receive a chunk from the WebSocket connection
        
        # Code to receive a chunk from WebSocket
    if chunk:
        # Call the handle_chunk function to process the chunk
        handle_chunk(chunk)
    # else:
    #     # If there's an error receiving the chunk, break out of the loop
    #     break  
    return 'image'

#  print("hello")
#     image_bytes = base64.b64decode(cap)
#     image = Image.open(BytesIO(image_bytes))
#     image.save('output.jpg', 'JPEG')
#     with open('output.jpg', 'rb') as f:
#         image_bytes = f.read()
#         path = Path('output.jpg').rglob("*.jpg")
#         for img_p in path:
#             try:
#                 img = PIL.Image.open(img_p)
#                 frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#                 cv2.imshow('video', frame_rgb)
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#             except PIL.UnidentifiedImageError:
#                     print("wrong")


def handle_chunk(chunk):
    # Convert the chunk to a NumPy array
    nparr = np.frombuffer(chunk, np.uint8)
    # Decode the array into a video frame
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the grayscale frame
    cv2.imshow('Gray', gray)
    cv2.waitKey(1)



# Close the OpenCV window
cv2.destroyAllWindows()
if __name__ == '__main__':
    app.run(debug=True)