# import base64
# import json
# import logging

# from flask import Flask
# from flask_sockets import Sockets

# from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# sockets = Sockets(app)
# CORS(sockets, support_credentials=True)

# HTTP_SERVER_PORT = 5000

# @sockets.route('/media')
# @cross_origin(supports_credentials=True)
# def echo(ws):
#     app.logger.info("Connection accepted")
#     # A lot of messages will be sent rapidly. We'll stop showing after the first one.
#     has_seen_media = False
#     message_count = 0
#     while not ws.closed:
#         message = ws.receive()
#         if message is None:
#             app.logger.info("No message received...")
#             continue

#         # Messages are a JSON encoded string
#         data = json.loads(message)

#         # Using the event type you can determine what type of message you are receiving
#         if data['event'] == "connected":
#             app.logger.info("Connected Message received: {}".format(message))
#         if data['event'] == "start":
#             app.logger.info("Start Message received: {}".format(message))
#         if data['event'] == "media":
#             if not has_seen_media:
#                 app.logger.info("Media message: {}".format(message))
#                 payload = data['media']['payload']
#                 app.logger.info("Payload is: {}".format(payload))
#                 chunk = base64.b64decode(payload)
#                 app.logger.info("That's {} bytes".format(len(chunk)))
#                 app.logger.info("Additional media messages from WebSocket are being suppressed....")
#                 has_seen_media = True
#         if data['event'] == "closed":
#             app.logger.info("Closed Message received: {}".format(message))
#             break
#         message_count += 1

#     app.logger.info("Connection closed. Received a total of {} messages".format(message_count))


# if __name__ == '__main__':
#     app.logger.setLevel(logging.DEBUG)
#     from gevent import pywsgi
#     from geventwebsocket.handler import WebSocketHandler

#     server = pywsgi.WSGIServer(('', HTTP_SERVER_PORT), app, handler_class=WebSocketHandler)
#     print("Server listening on: http://localhost:" + str(HTTP_SERVER_PORT))
#     server.serve_forever()
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
#     return render_template('http://192.168.137.77:8080/')

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
