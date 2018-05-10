import lcm
import numpy as np
import cv2
from exlcm import video_t

def my_handler(channel, data):
    msg = video_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    c = np.array(msg.stream).astype(np.uint8)
    data3 = np.ndarray(shape=(480,640,3), dtype=np.uint8,buffer=np.array(c))
    cv2.imshow('subFrame', data3)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        return
    
lc = lcm.LCM()
subscription = lc.subscribe("VideoTopic", my_handler)
print("start....")
try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
