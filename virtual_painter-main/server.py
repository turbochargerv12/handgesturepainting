from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

import numpy as np
import cv2
import json
import base64

app = Flask(__name__)
CORS(app, support_credentials=True)
# @app.route('/')
# def home():
#     return render_template('http://127.0.0.1:8080/')

@app.route('/data', methods=['POST','GET'])
@cross_origin(supports_credentials=True)
def handle_frame():
    if request.method == 'POST':
        frame = request.form.get('name')
        print(frame)
        # jpg_bytes = base64.b64decode(frame)
        # image = cv2.imdecode(np.frombuffer(jpg_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        # cv2.imshow('video', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print('hello')
    return 'successfully'


if __name__ == '__main__':
    app.run(debug=True)
# import cv2
# import numpy as np
# import websocket
# import json

# cap = cv2.VideoCapture(0)

# def on_message(ws, message):
#     # handle incoming messages from the client...
#     msg = message
#     return msg
    

# def on_error(ws, error):
#     # handle errors...
#     msg = error
#     return msg

# def on_close(ws,p,q):
#     # handle closed connection...
#     return 'close'

# def on_open(ws):
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         # convert the OpenCV frame to a JSON-serializable format
#         data = {'frame': frame.tolist()}
#         ws.send(json.dumps(data))

# websocket.enableTrace(True)
# ws = websocket.WebSocketApp('ws://localhost:8000/',
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
# ws.on_open = on_open
# ws.run_forever()

# if ws.connected:
#     print("success full")
# else:
#     print("no")

