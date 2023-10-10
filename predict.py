# ------------------------- import libraries
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import * # this module used for tracking
from datetime import datetime, timedelta

# ---------------------------- import model
model = YOLO('best.pt')

# Create a DataFrame to store the count data
df = pd.DataFrame(columns=['Date', 'Day of the week', 'CarCount', 'BikeCount', 'BusCount', 'TruckCount', 'Total'])
# Function to update the DataFrame and save it to CSV
def update_csv(car_count,bike_count,bus_count,truck_count):
    now = datetime.now()
    date = now.strftime("%d")
    day = now.strftime("%A")
    total_count = car_count + bike_count + bus_count + truck_count
    new_row = {'Date': date, 'Day of the week': day, 'CarCount': car_count, 'BikeCount': bike_count,
               'BusCount': bus_count, 'TruckCount': truck_count, 'Total': total_count}
    df.loc[len(df)] = new_row
    df.to_csv('counting_data.csv', index=False)


# -------------------------- add mouse option for finding the line x and y coordinate
area = [(283, 281), (203, 307), (549, 343), (562, 295)]
tracker = Tracker()
area_set = set()
car_count = set()
bike_count = set()
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


# Set the start time
start_time = datetime.now()
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
                bike_count.add(id)
            elif d == 1:
                truck_count.add(id)
            elif d== 2:
                car_count.add(id)
            elif d == 3:
                bus_count.add(id)
    # Check if 15 minutes have passed
    current_time = datetime.now()
    time_diff = current_time - start_time
    if time_diff.total_seconds() >= 120:  # 15 minutes = 900 seconds
        # Update the CSV and reset the counts
        update_csv(len(car_count), len(bike_count), len(bus_count), len(truck_count))
        car_count.clear()
        bike_count.clear()
        bus_count.clear()
        truck_count.clear()
        start_time = current_time
    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 255, 0), 1) # draw a box which we count the object in
    count = len(area_set)
    cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 255, 255), 1)  # show the count of car in the frame
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
