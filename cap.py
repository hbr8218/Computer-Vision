import cv2
import numpy


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id = 0
cap  = cv2.VideoCapture(0)
if not cap.isOpened():
    exit(0)

while True:

    ret, frame = cap.read()
    if ret is False:
        break
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,6)

    for (x,y,w,h) in face:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,0,255), 2)

        crop_gray = gray[y:y+h, x:x+w]
        crop_color = frame[y:y+h, x:x+w]
        # id += 1
        # folder = "img/"
        # image_name = folder+'my_pic' + str(id) +'.jpg'
        # cv2.imwrite(image_name, crop_gray)
        # print(image_name)
        # put text in image
        # cv2.putText(crop_color, "Hassan", (int(50), int(50)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        image = cv2.putText(crop_color, 'Hassan', (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255,255,255),2) 
        cv2.imshow("image",image)
        # #resize croped image 
        # image = cv2.resize(crop_gray,(32,32))
        # print(image.shape)
    
    c = cv2.waitKey(1)
    if c == 27:
        break
# frame.release()
cv2.destroyAllWindows()