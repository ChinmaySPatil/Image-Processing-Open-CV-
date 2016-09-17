import numpy as np
import cv2

#WHITE = np.array([255, 255, 255], np.uint8)
cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2(5,30,False)
detectShadows = False
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    one = fgmask[0:100, 0:640]
    two = fgmask[100:200, 0:640]
    three = fgmask[200:300, 0:640]
    cv2.imshow('one',one)
    cv2.imshow('two',two)
    cv2.imshow('three',three)

    a = cv2.countNonZero(one)
    b = cv2.countNonZero(two)
    c = cv2.countNonZero(three)

    if a>300:
         print('Motion in 1st block')
    if b>300:
         print('Motion in 2st block')
    if c>300:
         print('Motion in 3st block')

    #channel = frame-fgmask
    #cv2.imshow('frame',channel)
    k = cv2.waitKey(5) & 0xff
    if k == 10:
        break

cap.release()
cv2.destroyAllWindows()
