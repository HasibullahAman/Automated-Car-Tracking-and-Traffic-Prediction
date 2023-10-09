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


