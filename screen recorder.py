
import pyautogui
import cv2
from win32api import GetSystemMetrics
import numpy as np
import time

# screen regulation ke liye width and height

width =GetSystemMetrics(0)
height =GetSystemMetrics(1)

# save width and height
dim=(width,height)

# for tell the formate  , video writter cv2 ka fun h  , XVID capture the video mp4,sd api sb esme hi hote h

f= cv2.VideoWriter_fourcc(*"XVID")

output=cv2.VideoWriter("test.avi",f,30.0,dim)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

now_start_time = time.time()

dur = 10+4    #for complilation time 4 sec

end_time = now_start_time +dur

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow('Live', frame)
    c_time = time.time()

    if c_time>end_time:
        break
output.release()

print("---END---")



