# https://docs.ultralytics.com/guides/queue-management/#how-can-i-use-ultralytics-yolo11-for-real-time-queue-management

import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(0)
queue_region = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

queuemanager = solutions.QueueManager(
    model="yolo11n.pt",
    region=queue_region,
    line_width=3,
    show=True,
)

while cap.isOpened():
    success, im0 = cap.read()
    if success:
        results = queuemanager(im0)

cap.release()
cv2.destroyAllWindows()
