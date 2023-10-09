# ------------------------- import libraries
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO

# ---------------------------- import model
model = YOLO('best.pt')


# -------------------------- add mouse option for finding the line x and y coordinate
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# -----------------------------------import video file
cap = cv2.VideoCapture('vidyolov8.mp4')
# ----------------------------------- Read the class file
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

# ---------------------------------- Detect and assign rounding box + class name
count = 0
while True:

    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500))

    results = model.predict(frame)
# ---------------------------- draw a lin and display the class name
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype('float')
    for index,row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.putText(frame, str(c), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0,0), 1)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
