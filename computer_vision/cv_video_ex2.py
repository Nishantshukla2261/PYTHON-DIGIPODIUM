import cv2
import numpy as np

video =cv2.VideoCapture(r"D:\Downloads\WhatsApp Video 2023-12-06 at 4.46.31 PM.mp4")## address dalna hai kisi bhi video ka,copy as path
while True:
    status,frame=video.read()
    if not status:break
    small_frame=cv2.resize(frame,(0,0),fx=0.3,fy=0.3) # original size se 30% km 
    gray_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2GRAY)
    rgb_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    inv_frame = rgb_frame + 10
    print('rgb',rgb_frame[:1, :2])
    print('invert',rgb_frame[:1, :2])


    cv2.imshow("Video output",small_frame)
    cv2.imshow("Video output2",gray_frame)
    cv2.imshow("Video output3",rgb_frame)
    cv2.imshow("Video output4",inv_frame)
    if cv2.waitKey(1)==27:  ## 27 means escape key ,30 enter k kiye (10) bhi likh sakte h 0 nhi raklh sakte bas
        break
video.release()
cv2.destroyAllWindows()