import os
import cv2
import numpy as np

import torch
import torchvision

from torchvision.models import detection
from torchvision.utils import draw_bounding_boxes

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

coco_classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 
                'truck', 'boat', 'traffic light', 'fire hydrant', 'street sign', 'stop sign', 
                'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 
                'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 'shoe', 
                'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
                'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 
                'tennis racket', 'bottle', 'plate', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 
                'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 
                'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 
                'dining table', 'window', 'desk', 'toilet', 'door', 'tv', 'laptop', 'mouse', 
                'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 
                'refrigerator', 'blender', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 
                'hair drier', 'toothbrush', 'hair brush']
coco_classes = dict(zip(range(1, 1 + len(coco_classes)), coco_classes))
# print('coco_classes:', coco_classes)

model = detection.fasterrcnn_resnet50_fpn(weights=detection.FasterRCNN_ResNet50_FPN_Weights.DEFAULT).to(device)
model.eval()

def detection(image):
    image = torch.from_numpy(image).permute((2, 0, 1)).unsqueeze(0) / 255.0
    predictions = model(image)

    labels = predictions[0]['labels'].detach().numpy()
    bboxes = predictions[0]['boxes'].detach().numpy()
    scores = predictions[0]['scores'].detach().numpy()
    detection_output = (image.squeeze(0) * 255).type(torch.uint8).permute((1, 2, 0)).numpy()

    for (label, bbox, score) in zip(labels, bboxes, scores):
        if score > 0.7:
            x1, y1, x2, y2 = np.round(bbox).astype(np.int16)
            cv2.rectangle(detection_output, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(detection_output, coco_classes[label], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    return detection_output
