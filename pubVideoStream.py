import lcm
import time
import numpy as np
import cv2
from exlcm import video_t

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

cap = cv2.VideoCapture(0)
frency = 0
while (True):
    ret, frame = cap.read()
    cv2.imshow('origialVideo', frame)
    frency = frency+1
    if frency == 50:
        msg = video_t()
        msg.timestamp = int(time.time() * 1000000)
        originalArray = frame.ravel()
        msg.stream= list(np.array(frame.flatten()))
        lc.publish("VideoTopic", msg.encode())
        frency = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWinowds()


