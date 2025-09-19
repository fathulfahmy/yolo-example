# https://docs.ultralytics.com/guides/instance-segmentation-and-tracking/#note

import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"

# Video writer
# w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# video_writer = cv2.VideoWriter("instance-segmentation.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init InstanceSegmentation
isegment = solutions.InstanceSegmentation(
    show=True,  # display the output
    model="yolo11n-seg.pt",  # model="yolo11n-seg.pt" for object segmentation using YOLO11.
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = isegment(im0)
    # video_writer.write(results.plot_im)

cap.release()
# video_writer.release()
cv2.destroyAllWindows()
