import numpy as np
import cv2

video = cv2.VideoCapture(0)

lower_red = np.array([0,150 ,20])
upper_red = np.array([15 ,255,255])


while True :
    success , img = video.read()
    image = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image , lower_red , upper_red)

    cv2.imshow("mask" , mask)
    cv2.imshow("webcam", img)

    cv2.waitKey(2)
