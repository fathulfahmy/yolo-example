# https://docs.ultralytics.com/guides/trackzone/#how-do-i-track-objects-in-a-specific-area-or-zone-of-a-video-frame-using-ultralytics-yolo11

import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"
# w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
region_points = [(150, 150), (1130, 150), (1130, 570), (150, 570)]

# Video writer
# video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init trackzone (object tracking in zones, not complete frame)
trackzone = solutions.TrackZone(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo11n.pt",
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print(
            "Video frame is empty or video processing has been successfully completed."
        )
        break
    results = trackzone(im0)
    # video_writer.write(results.plot_im)

cap.release()
# video_writer.release()
cv2.destroyAllWindows()
