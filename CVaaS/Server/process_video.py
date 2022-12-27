import cv2
import base64
import numpy as np

import restoration
import fasterrcnn_detection

# possible choices: 'real_denoising', 'super_resolution', 'contrast_enhancement', 'lowlight_enhancement'
task = 'real_denoising'
vid = cv2.VideoCapture('demo01.mp4')
model = restoration.load_model(task)
print('Model Loaded for task:', task)

while True:
    ret, degraded_image = vid.read()
    if not ret:
        break
    
    # perform task and enhance degraded_image
    restored_image = restoration.inference(model, degraded_image)
    # print('Image Restored for task:', task)
    # perform fasterrcnn detection
    res_det_image = fasterrcnn_detection.detection(restored_image)
    deg_det_image = fasterrcnn_detection.detection(degraded_image)
    # print('Faster RCNN detection performed for task:', task)

    cv2.imshow('degraded_image', degraded_image)
    cv2.imshow('restored_image', restored_image)
    cv2.imshow('res_det_image', res_det_image)
    cv2.imshow('deg_det_image', deg_det_image)
    
    if cv2.waitKey(1) & 0xFF == 'q':
        break

cv2.destroyAllWindows()
