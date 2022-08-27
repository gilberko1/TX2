import cv2
import os
#os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "video_codec;h264_cuvid"
#cap = cv2.VideoCapture(url)
cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! queue ! appsink drop=1", cv2.CAP_GSTREAMER)
if not cap.isOpened():
   print(cv2.getBuildInformation())
   print('Failed to open camera')
   exit

cv2.namedWindow('Demo', cv2.WINDOW_AUTOSIZE)

# Run for 300 frames
for i in range(300):
        ret_val, img = cap.read();
        if not ret_val:
                break

        cv2.imshow('Demo', img);
        cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()