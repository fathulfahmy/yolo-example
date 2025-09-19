# https://docs.ultralytics.com/guides/workouts-monitoring/

import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (
    int(cap.get(x))
    for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS)
)

gym = solutions.AIGym(
    line_width=2,
    show=True,
    kpts=[6, 8, 10],
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = gym(im0)

cv2.destroyAllWindows()
