import lcm
import numpy as np
import cv2
from exlcm import video_t
import face_recognition

wenjun_image = face_recognition.load_image_file("wenjun.jpg")
wenjun_face_encoding = face_recognition.face_encodings(wenjun_image)[0]

known_face_encodings = [
    wenjun_face_encoding

]
known_face_names = [
    "Wenjun Ma"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


def my_handler(channel, data):
    msg = video_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    c = np.array(msg.stream).astype(np.uint8)
    frame = np.ndarray(shape=(480,640,3), dtype=np.uint8,buffer=np.array(c))
    # small_frame = cv2.resize(c, (0, 0), fx=0.25, fy=0.25)
    # rgb_small_frame = small_frame[:, :, ::-1]
    # rgb_small_frame = c[:, :, ::-1]
    global process_this_frame
    global face_locations
    global face_encodings
    global face_names
    global known_face_encodings
    global known_face_names
    global wenjun_face_encoding
    global wenjun_image



    rgb_small_frame =frame
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)

                name = known_face_names[first_match_index]



            face_names.append(name)

    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 1
        right *= 1
        bottom *= 1
        left *= 1
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        print(face_locations)

    cv2.imshow('DetectFace', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        return
    
lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
subscription = lc.subscribe("VideoTopic", my_handler)
print("start....")
try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
