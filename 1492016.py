import numpy as np
import cv2

def value(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        if (0 <= x <= 400) & (0 <= y <= 400):
           print ('1')
           
cam = cv2.VideoCapture(1)

while(cam.isOpened()):

    ret,frame = cam.read()


#print  (cx,cy)
    cv2.setMouseCallback('image',value)
    cv2.imshow("image",frame)


    k = cv2.waitKey(1) & 0xFF

    if k== 27:
        break
cv2.destroyAllWindows()
    
