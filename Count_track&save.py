# import libraries

import cv2
import numpy as np  # Importing NumPy library for numerical operations
from ultralytics import YOLO  # Importing YOLO from ultralytics package
import pandas as pd  # Importing Pandas library for data manipulation and analysis
import time  # Importing Time module for timing operations

# ------------------------------ Import Model

# import Automatic-car-tracking model
model=YOLO('./Model.pt')
# fining the mouse position
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :
        colorsBGR = [x, y]
        print(colorsBGR)

# ----------------------------- Read Class
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")


# --------------------------------- Read video
isopen = True
while isopen:
    cap1 = cv2.VideoCapture('video5.mp4')
    cap2 = cv2.VideoCapture('Second_part.mp4')
    cap3 = cv2.VideoCapture('video6.mp4')
    cap4 = cv2.VideoCapture('second_part-2.mp4')

    first_frame_time = time.time()

    while (time.time() - first_frame_time) < 15:

        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or frame1 is None:
            break

        if not ret2 or frame2 is None:
            break

        new_size1 = cv2.resize(frame1, (820, 420))
        new_size2 = cv2.resize(frame2, (820, 420))

        final_frame1 = new_size1[:, :600]
        final_frame2 = new_size2[:, :-120]

        area1 = [(0, 418), (0, 233), (255, 0), (429, 1), (569, 204), (592, 417)]
        area2 = [(600, 418), (600, 304), (880, 50), (1030, 40), (1300, 416)]

        combined_frame1 = np.concatenate((final_frame1, final_frame2), axis=1)

        # combined_frame= np.concatenate((combined_frame1,combined_frame2), axis=0)

        result1 = model.predict(combined_frame1)

        a = result1[0].boxes.data

        px1 = pd.DataFrame(a).astype("float")
        #    print(px)

        count1 = []

        for index, row in px1.iterrows():
            #        print(row)
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]

            cx = int(x1 + x2) // 2
            cy = int(y1 + y2) // 2

            results1 = cv2.pointPolygonTest(np.array(area1, np.int32), (cx, cy), False)
            results2 = cv2.pointPolygonTest(np.array(area2, np.int32), (cx, cy), False)

            if results1 >= 0 or results2 >= 0:
                cv2.rectangle(combined_frame1, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(combined_frame1, (cx, cy), 3, (0, 0, 255), -1)
                cv2.putText(combined_frame1, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

                # print(c)
                count1.append(c)
        # ================================================================================================================

        print('Amounts of cars in Frame1: ', len(count1))

        # cv2.putText(combined_frame, str(len(count)), (50, 60), cv2.FONT_HERSHEY_PLAIN, .5, (255, 0, 255), 1)

        cv2.polylines(combined_frame1, [np.array(area1, np.int32)], True, (255, 0, 0), 2)
        cv2.polylines(combined_frame1, [np.array(area2, np.int32)], True, (255, 0, 0), 2)

        # cv2.imshow('combined_video1', combined_frame1)

        if cv2.waitKey(0) == ord('q'):
            isopen = False
            break

    # if isopen == False:
    #    break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

    # ====================================================== Process Frame ==========================================================
    sencond_frame_time = time.time()

    while (time.time() - sencond_frame_time) < 15:

        ret3, frame3 = cap3.read()
        ret4, frame4 = cap4.read()

        if not ret3 or frame3 is None:
            break

        if not ret4 or frame4 is None:
            break

        new_size3 = cv2.resize(frame3, (820, 420))
        new_size4 = cv2.resize(frame4, (820, 420))

        final_frame3 = new_size3[:, 140:-30]
        final_frame4 = new_size4[:, 140:-30]

        area3 = [(0, 418), (0, 212), (228, 0), (595, 0), (648, 418)]
        area4 = [(652, 416), (653, 194), (895, 0), (1217, 0), (1300, 418)]

        combined_frame2 = np.concatenate((final_frame3, final_frame4), axis=1)

        result2 = model.predict(combined_frame2)

        b = result2[0].boxes.data

        px2 = pd.DataFrame(b).astype("float")

        count2 = []

        for index, row in px2.iterrows():
            # print('this is the rows: ', row)
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]

            cx = int(x1 + x2) // 2
            cy = int(y1 + y2) // 2

            results3 = cv2.pointPolygonTest(np.array(area3, np.int32), (cx, cy), False)
            results4 = cv2.pointPolygonTest(np.array(area4, np.int32), (cx, cy), False)

            if results3 >= 0 or results4 >= 0:
                cv2.rectangle(combined_frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(combined_frame2, (cx, cy), 3, (0, 0, 255), -1)
                cv2.putText(combined_frame2, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

                # print(c)
                count2.append(c)

        print('Amounts of cars in Frame2: ', len(count2))

        cv2.polylines(combined_frame2, [np.array(area3, np.int32)], True, (255, 0, 0), 2)
        cv2.polylines(combined_frame2, [np.array(area4, np.int32)], True, (255, 0, 0), 2)

        cv2.imshow('combined_video2', combined_frame2)

        if cv2.waitKey(0) == ord('q'):
            isopen = False
            break

    cap3.release()
    cap4.release()
    cv2.destroyAllWindows()

    # if isopen == False:
    #     break

cv2.destroyAllWindows()