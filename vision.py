import numpy as np
import cv2

video = cv2.VideoCapture(0)

lower_red = np.array([100, 120 ,20])
upper_red = np.array([132 ,250,255])


while True :
    success , img = video.read()
    image = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image , lower_red , upper_red)
    
    contoues , hierarchy = cv2.findContours(mask , cv2.RETR_EXTRERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contours) != 0:
        for contour in contours :
            if cv2.contourArea(contour) > 500: 
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(img , (x,y) , (x+w,y+h) (0,0,255) , 3)

    cv2.imshow("mask" , mask)
    cv2.imshow("webcam", img)

    cv2.waitKey(2)
