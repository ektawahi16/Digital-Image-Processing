#Write a program to implement the power law transformation. 
#Show the variations in the image for different values of gamma.

import numpy as np
from cv2 import cv2

img = cv2.imread("C:/Users/ekta/Desktop/dog.jpg")
# Apply Gamma=2.2
gamma1 = np.array(255*(img/255)**2.2,dtype='uint8')
#Apply Gamma=0.4 
gamma2 = np.array(255*(img/255)**0.4,dtype='uint8')
img3 = cv2.hconcat([gamma1,gamma2])
cv2.imwrite('output4.png',img3)