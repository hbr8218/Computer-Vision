import cv2
import numpy as np

cap = cv2.VideoCapture('eye.mp4')

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    roi_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Filter noise
    roi_gray = cv2.GaussianBlur(roi_gray, (7,7), 0)

    # Draw thresholds
    _,threshold = cv2.threshold(roi_gray, 5, 255, cv2.THRESH_BINARY_INV)

    # Draw contours 
    # _,contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    # for contour in contours:
    #     cv2.drawContours(frame, [contour], -1, (0,0,255), 3)
    #     break
    # # cv2.imshow("Countour",contour)
    cv2.imshow("Threshold",threshold)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.DestroyAllWindows()