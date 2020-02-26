import cv2
import numpy as np

face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    exit(0)

# Infinite loop to Capture the real time video
while True:

    ret, frame = cap.read()

    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    if ret == False:
        print(ret)
        break
    # # cascadeClassifier takes gray_scaled images so convert frame in gray scale
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # # Intantiate face from face_cascade
    face_detected = face_cascade.detectMultiScale(gray_frame,1.5,5)

    # # Draw a rectangle that enclose the detected face
    for (x,y,w,h) in face_detected:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # convert detected face into gray scale
        gray_d_face = gray_frame[y:y+h,x:x+h]

        # convert detected face into color frame
        clr_d_face = frame[y:y+h,x:x+w]

        # Instantiate eye from eye_cascade
        eyes = eye_cascade.detectMultiScale(gray_d_face)
        # Enclose eyes with rectangles
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(clr_d_face, (ex,ey), (ex+ew,ey+eh), (0,255,0), 1)
            # gray_d_eyes = gray_d_face[ey:ey+eh,ex+ex+ew]
        

        # Display frame,gray_d_face
        cv2.imshow("Input",frame)
    
    # ms per frame
    key = cv2.waitKey(3)
    if key == 27:
        break

# Destroy all windows    
cv2.destroyAllWindows()