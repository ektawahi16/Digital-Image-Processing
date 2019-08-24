#Write a program to implement the log transformation of a gray image

from cv2 import cv2
import numpy as np

img  = cv2.imread("C:/Users/ekta/Desktop/dog.jpg")
img_log = (np.log(img+1)/(np.log(1+np.max(img))))*255
img_log = np.array(img_log,dtype=np.uint8)
cv2.imwrite('output3.png',img_log )
