import cv2
import base64
import numpy as np

from flask import jsonify
from flask import Flask, request
from flask_cors import CORS, cross_origin

import restoration
import fasterrcnn_detection

app = Flask('CVaaS')
CORS(app)

def cv_engine(image, task):
    TAG = '[cv_engine]'
    print(TAG, '[starts]')
    # perform task and enhance image
    model = restoration.load_model(task)
    print('Model Loaded for task:', task)
    print(model)
    restored_image = restoration.inference(model, image)
    print('Image Restored for task:', task)
    # perform fasterrcnn detection
    detection_image = fasterrcnn_detection.detection(restored_image)
    print('Faster RCNN detection performed for task:', task)
    return detection_image

def read_image(image_data):
    TAG = '[read_image]'
    print(TAG, '[starts]')
    image_data = base64.decodebytes(image_data)
    with open('temp_image.jpg', 'wb') as f:
        f.write(image_data)
        f.close()
    image = cv2.imread('temp_image.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def encode_image(image):
    TAG = '[encode_image]'
    print(TAG, '[starts]')
    ret, data = cv2.imencode('.jpg', image)
    encoded_img = 'data:image/jpeg;base64,' + base64.b64encode(data).decode('utf-8')
    return encoded_img

# This is the server to handle requests and get images from client
@app.route('/process_image', methods=['POST'])
def process_image():
    TAG = '[process_image]'
    print(TAG, '[starts]')
    if not request.json:
        return 'Server Error!', 500
    
    header_len = len('data:image/jpeg;base64,')
    image_data = request.json['image_data'][header_len:].encode()
    operation = request.json['operation']
    
    image = read_image(image_data)
    img_out = cv_engine(image, operation)    
    image_data = encode_image(img_out)
    
    result = {'image_data': image_data, 'msg':'Operation Completed'}
    return result, 200

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
