
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
# from main import framework

import numpy as np
from PIL import Image
from io import BytesIO
import cv2
import io
import json
import base64

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def home():
    return 'succesful'

@app.route('/image', methods=['POST'])
@cross_origin(supports_credentials=True)
def process_image():
    cap = request.get_data()
    print(cap)
    # image = Image.open(BytesIO(cap))
    # import matplotlib.pyplot as plt

    # plt.imshow(image)
    # plt.show()
    # image_bytes = io.BytesIO(cap)
    # image_array = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    # image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("img",image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # framework(cap)
    return 'image'

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


