import cv2
from datetime import datetime

# A list of the paths of your videos
videos = ['log/output2024-10-14T18-32-46-958552.mp4','log/output2024-10-14T18-33-46-969000.mp4', 'log/output2024-10-14T18-34-47-006595.mp4', 'log/output2024-10-14T18-35-47-019932.mp4', 'log/output2024-10-14T18-36-47-062084.mp4']

clip1 = cv2.VideoCapture('log/output2024-10-14T18-32-46-958552.mp4')

width  = clip1.get(cv2.CAP_PROP_FRAME_WIDTH)
height = clip1.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps    = clip1.get(cv2.CAP_PROP_FPS) 

print("Date start:", datetime.now())

# Create a new video
video = cv2.VideoWriter("log/new_stitched_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(width), int(height)))

# Write all the frames sequentially to the new video
for v in videos:
    print("Picked up:", v, "at", datetime.now())
    curr_v = cv2.VideoCapture(v)
    while curr_v.isOpened():
        # Get return value and curr frame of curr video
        r, frame = curr_v.read()
        if not r:
            break
        # Write the frame
        video.write(frame)

# Save the video
video.release()

print("Date ready:", datetime.now())
