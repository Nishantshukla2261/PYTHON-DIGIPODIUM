import cv2
import numpy as np

video =cv2.VideoCapture(0)## camera on ho jayega 
while True:
    status,frame=video.read()
    if not status:break
    cv2.imshow("webcam output",frame)
    if cv2.waitKey(1)==27: # escape key  ## 27 means escape key ,30 enter k kiye (10) bhi likh sakte h 0 nhi raklh sakte bas
        break
video.release()
cv2.destroyAllWindows()