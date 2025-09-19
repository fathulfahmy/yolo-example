# https://docs.ultralytics.com/guides/trackzone/#real-world-applications
import cv2

from ultralytics import solutions

video_path = 0
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"

# Define region points
region_points = [(150, 150), (1130, 150), (1130, 570), (150, 570)]

# Video writer
# w, h, fps = (
#     int(cap.get(x))
#     for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS)
# )
# video_writer = cv2.VideoWriter(
#     "trackzone_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h)
# )

# Init trackzone (object tracking in zones, not complete frame)
trackzone = solutions.TrackZone(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo11n.pt",  # use any model that Ultralytics support, i.e. YOLOv9, YOLOv10
    # line_width=2,  # adjust the line width for bounding boxes and text display
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = trackzone(im0)

    # print(results)  # access the output

    # video_writer.write(results.plot_im)  # write the video file

cap.release()
# video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
