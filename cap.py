import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap  = cv2.VideoCapture(0)
total_frame = 0
id = 0

if not cap.isOpened():
    exit(0)

#Capture images per 25 frame
frameFrequency=25

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,6)
    
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,0,255), 2)
        id += 1
        image_name = 'my_pic' + str(id) +'.jpg'
        cv2.imwrite(image_name, frame)
        cv2.imshow('Input',frame)
        print(image_name)
    # total_frame += 1
    # if total_frame%frameFrequency == 0:
    #     id += 1
    #     image_name = 'my_pic' + str(id) +'.jpg'
    #     cv2.imwrite(image_name, frame)
    #     cv2.imshow('Input',frame)
    #     print(image_name)
    c = cv2.waitKey(1)
    if c == 27:
        break
cv2.release()
cv2.destroyAllWindows()