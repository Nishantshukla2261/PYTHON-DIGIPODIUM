import cv2
import numpy as np

video =cv2.VideoCapture(0)## camera on ho jayega 
while True:
    status,frame=video.read()
    if not status:break

    cv2.rectangle(frame,(50,50),(200,300),(255,255,255),-1) ## white color ka box dikhega, -1 fills box
    cv2.circle(frame,(125,175),50,(0,0,255),-1) ## white color ka box dikhega, -1 fills box
    cv2.putText(frame,'One',(125,175),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1) # 1 means normal scale,0.5 means half,2 means double
    


    cv2.imshow("webcam output",frame)
    if cv2.waitKey(1)==27: # escape key  ## 27 means escape key ,30 enter k kiye (10) bhi likh sakte h 0 nhi raklh sakte bas
        break
video.release()
cv2.destroyAllWindows()