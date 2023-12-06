import cv2
import numpy as np
im1 = cv2.imread("computer_vision/python_ai.png")
print(im1.shape)
print(im1.ndim)
# im1 = im1*255  # image ko 255 ka area leke chal rha
im1 = im1[0:200:2 ] ## height , weight  slicing
cv2.imshow("image 1",im1)
cv2.waitKey(0)
