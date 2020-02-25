import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    id=1
    ret, frame = cap.read()
    # print(frame)
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,6)
    
    # cv2.imwrite('frame'+str(id)+'.png',face)

    for (x,y,w,h) in face:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,0,255), 2)
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = frame[y:y+h, x:x+w]
        # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('Input', frame)
    

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()