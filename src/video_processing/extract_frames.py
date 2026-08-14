import cv2 

video_path = "data/raw/match1.mp4"
video = cv2.VideoCapture(video_path) #opens & access frames
print(video.isOpened())

fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(total_frames)
duration = total_frames/fps
print(duration)

success, frame = video.read() #gives access to video
print(success)
cv2.imwrite('data/processed/first_frame.jpg', frame) #saves image

video.set(cv2.CAP_PROP_POS_FRAMES, 9000) #changing current frame position
success, frame = video.read()
cv2.imwrite("data/processed/frame_5min.jpg", frame)

interval = 60
# frame_number = int(interval * fps)
# print(frame_number)
# video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
# success, frame = video.read()
# cv2.imwrite("data/processed/frame_1min.jpg", frame)

current_time = 0
while current_time <= duration:
    frame_number = int(current_time * fps)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = video.read()
    cv2.imwrite("data/processed/frame_1min.jpg", frame)