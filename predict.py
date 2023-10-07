# ------------------------- Import Library

import cv2
import numpy as np  # Importing NumPy library for numerical operations
from ultralytics import YOLO  # Importing YOLO from ultralytics package
import pandas as pd  # Importing Pandas library for data manipulation and analysis
import time  # Importing Time module for timing operations

# ------------------------------ Import Model

# in this line we import the model we trained in Car Object Detection file

model = YOLO('./best.pt')


# fining the mouse position
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


# cv2.namedWindow('combined_video1')
# cv2.setMouseCallback('combined_video1', RGB)
# cv2.namedWindow('combined_video2')
# cv2.setMouseCallback('combined_video2', RGB)

# ----------------------------- Read Class
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
print(class_list)
# count=0


# --------------------------------- Read video
isopen = True
while isopen:
    cap1 = cv2.VideoCapture('download.mp4')

