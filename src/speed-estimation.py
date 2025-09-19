# https://docs.ultralytics.com/guides/speed-estimation/#how-do-i-estimate-object-speed-using-ultralytics-yolo11

import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(video_path)
# w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# video_writer = cv2.VideoWriter("speed_estimation.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize SpeedEstimator
speedestimator = solutions.SpeedEstimator(
    model="yolo11n.pt",
    show=True,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break
    results = speedestimator(im0)
    # video_writer.write(results.plot_im)

cap.release()
# video_writer.release()
cv2.destroyAllWindows()
