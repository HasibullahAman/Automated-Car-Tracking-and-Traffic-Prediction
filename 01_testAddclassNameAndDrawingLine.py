# # ------------------------- import libraries
# import cv2
# import pandas as pd
# import numpy as np
# from ultralytics import YOLO
#
# # ---------------------------- import model
# model = YOLO('best.pt')
#
# # -------------------------- add mouse option for finding the line x and y coordinate
# def RGB(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         colorsBGR = [x, y]
#         print(colorsBGR)
#
# cv2.namedWindow('RGB')
# cv2.setMouseCallback('RGB', RGB)
#
# # -----------------------------------import video file
# cap = cv2.VideoCapture('vidyolov8.mp4')
#
# # ----------------------------------- Read the class file
# my_file = open("coco.txt", "r")
# data = my_file.read()
# class_list = data.split("\n")
#
# # ---------------------------------- Detect and assign rounding box + class name
# count = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     count += 1
#     if count % 3 != 0:
#         continue
#     frame = cv2.resize(frame, (1020, 500))
#
#     results = model.predict(frame)
#
#     # Draw line and display class name for each detected object
#     if isinstance(results, list):
#         for result in results[0].xyxy:
#             x1, y1, x2, y2, conf, cls = result
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cls_name = class_list[int(cls)]
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, cls_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#     else:
#         for result in results.xyxy:
#             x1, y1, x2, y2, conf, cls = result
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cls_name = class_list[int(cls)]
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, cls_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#
#     cv2.imshow('RGB', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()




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
bus_count = 0
car_count = 0
truck_count = 0
bike_count = 0
count = 0
class_counts = pd.DataFrame(columns=['Date', 'Day of Week', 'Time', 'Buses', 'Cars', 'Trucks', 'Bikes', 'Total'])

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
        if 'bike' in c:
            bus_count += 1
        elif 'truck' in c:
            car_count += 1
        elif 'car' in c:
            truck_count += 1
        elif 'bus' in c:
            bike_count += 1
        if results >= 0:
            # show the center of object
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            # Draw a line when detect
            # cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 1)
            # show the object ID when detect
            # cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)
            area_set.add(id)
    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 255, 0), 1) # draw a box which we count the object in
    count = len(area_set)
    class_counts.loc[len(class_counts)] = ["date", "day_of_week", "time", bus_count, car_count, truck_count, bike_count,bus_count + car_count + truck_count + bike_count]
    if count % (15 * 60 * 3) == 0:  # Every 15 minutes (assuming 3 frames per second)
        class_counts.to_csv('class_count.csv', index=False)
    cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 255, 255), 1)  # show the count of car in the frame
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
# class_counts.to_csv('class_counts.csv', index=False)
cap.release()
cv2.destroyAllWindows()

