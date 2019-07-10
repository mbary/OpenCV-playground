import numpy as np
import sys
import cv2

arg = str(sys.argv[1])

image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

# We are supplying NumPy array slices to extract a rectangular region of the image, 
# starting at (240, 30) and ending at (335,120). The order in which we supply the 
# indexes to the crop may seem counterintuitive; however, remember that OpenCV represents 
# images as NumPy arrays with the the height first and the width second. 
# This means that we need to supply our y-axis values before our x-axis.
cropped = image[30:120, 245:335]

cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)
