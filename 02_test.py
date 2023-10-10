# Import the required libraries
import cv2
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ultralytics import YOLO
from tracker import *

# Create a DataFrame to store the count data
df = pd.DataFrame(columns=['Date', 'Day of the week', 'CarCount', 'BikeCount', 'BusCount', 'TruckCount', 'Total'])

# Function to update the DataFrame and save it to CSV
def update_csv(car_count, bike_count, bus_count, truck_count):
    now = datetime.now()
    date = now.strftime("%d")
    day = now.strftime("%A")
    total_count = car_count + bike_count + bus_count + truck_count
    new_row = {'Date': date, 'Day of the week': day, 'CarCount': car_count, 'BikeCount': bike_count, 'BusCount': bus_count, 'TruckCount': truck_count, 'Total': total_count}
    df.loc[len(df)] = new_row
    df.to_csv('counting_data.csv', index=False)

# Import the YOLO model
model = YOLO('best.pt')
area = [(283, 281), (203, 307), (549, 343), (562, 295)]
# -----------------------------------import video file
cap = cv2.VideoCapture('FirstVideo.mp4')
# Initialize the variables
tracker = Tracker()
area_set = set()

# Initialize the counts
car_count = 0
bike_count = 0
bus_count = 0
truck_count = 0

# Set the start time
start_time = datetime.now()

# Main loop for video processing
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform the detection
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)

    # Process the detected objects
    object_list = []
    for bbox in results[0].xyxy:
        x1, y1, x2, y2, conf, cls = bbox.tolist()
        cls = int(cls)
        if cls in [0, 1, 2, 3]:  # Consider only car, bike, bus, and truck
            object_list.append([int(x1), int(y1), int(x2), int(y2)])

    # Update the tracker and counts
    bbox_id = tracker.update(object_list)
    for bbox in bbox_id:
        x1, y1, x2, y2, obj_id = bbox
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        results = cv2.pointPolygonTest(np.array(area, np.int32), (cx, cy), False)
        if results >= 0:
            area_set.add(obj_id)
            if cls == 0:
                bike_count += 1
            elif cls == 1:
                truck_count += 1
            elif cls == 2:
                car_count += 1
            elif cls == 3:
                bus_count += 1

    # Check if 15 minutes have passed
    current_time = datetime.now()
    time_diff = current_time - start_time
    if time_diff.total_seconds() >= 120:  # 15 minutes = 900 seconds
        # Update the CSV and reset the counts
        update_csv(car_count, bike_count, bus_count, truck_count)
        car_count = 0
        bike_count = 0
        bus_count = 0
        truck_count = 0
        start_time = current_time

    # Display the frame with counts
    # ...

# Release the video capture and destroy windows
cap.release()
cv2.destroyAllWindows()