import cv2
import numpy as np

video =cv2.VideoCapture(r"D:\Downloads\WhatsApp Video 2023-12-06 at 4.46.31 PM.mp4")## address dalna hai kisi bhi video ka,copy as path
while True:
    status,frame=video.read()
    if not status:break
    cv2.imshow("Video output",frame)
    if cv2.waitKey(1)==27:  ## 27 means escape key ,30 enter k kiye (10) bhi likh sakte h 0 nhi raklh sakte bas
        break
video.release()
cv2.destroyAllWindows()