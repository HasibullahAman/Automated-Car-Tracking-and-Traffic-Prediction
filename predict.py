# ------------------------- import libraries
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import * # this module used for tracking

# ---------------------------- import model
model = YOLO('best.pt')


# -------------------------- add mouse option for finding the line x and y coordinate
area = [(283, 281), (203, 307), (549, 343), (562, 295)]
tracker = Tracker()
area_set = set()
car_count = set()
bike_cout = set()
bus_count = set()
truck_count = set()
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# -----------------------------------import video file
cap = cv2.VideoCapture('FirstVideo.mp4')
# ----------------------------------- Read the class file
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

# ---------------------------------- Detect and assign rounding box + class name
count = 0
while True:

    ret, frame = cap.read()
    # two variable:
        # ret, which indicates whether a frame was successfully read (True or False)
        # and frame, which is the actual frame/image data.
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500)) # set the size of frame
    results = model.predict(frame) # make prediction
    # ---------------------------- draw a lin and display the class name
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype('float')
    list = []
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'car' or 'truck' or 'bike' or 'bus' in c:
            list.append([x1, y1, x2,  y2])
    bbox_id = tracker.update(list)
    for bbox in bbox_id:
        x3, y3, x4, y4, id= bbox
        cx = int(x3+x4) // 2
        cy = int(y3+y4) // 2
        results = cv2.pointPolygonTest(np.array(area, np.int32), (cx, cy), False)
        if results >= 0:
            # show the center of object
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            # Draw a line when detect
            # cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
            # show the object ID when detect
            # cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)
            area_set.add(id)
            if d == 0:
                bike_cout.add(id)
            elif d == 1:
                truck_count.add(id)
            elif d== 2:
                car_count.add(id)
            elif d == 3:
                bus_count.add(id)
    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 255, 0), 1) # draw a box which we count the object in
    count = len(area_set)
    cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 255, 255), 1)  # show the count of car in the frame
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
