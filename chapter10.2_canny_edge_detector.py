"""

The Canny edge detector is a multi-step process. 
It involves blurring the image to remove noise, computing Sobel gradient images in the x and y direction, 
suppressing edges, and finally a hysteresis thresholding stage that determines if a pixel is “edge-like” or not.
"""

import sys
import cv2
import numpy as np

arg = str(sys.argv[1])
image = cv2.imread(arg)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.GaussianBlur(image, (5,5),0)

cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30,150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
