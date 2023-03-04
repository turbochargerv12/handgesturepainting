from flask import Flask
import numpy as np
import cv2
import base64

app = Flask(__name__)
@app.route('/')
# def hello():
#     return 'Hello, world!'
def handle_frame(frame):
    jpg_bytes = base64.b64decode(frame)
    image = cv2.imdecode(np.frombuffer(jpg_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow('video', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    app.run(debug=True)
