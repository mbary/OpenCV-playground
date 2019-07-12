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

# y ap- plying a blur prior to edge detection, we will help remove
# “noisy” edges in the image that are not of interest to us. 
# Our goal here is to find only the outlines of the coins.
image = cv2.GaussianBlur(image, (5,5),0)

cv2.imshow("Blurred", image)

# The first argument we supply is our blurred, grayscale image. 
# Then, we need to provide two values: threshold1 and threshold2.

# Any gradient value larger than threshold2 is considered to be an edge. 
# Any value below threshold1 is considered not to be an edge. 
# Values in between threshold1 and threshold2 are either classified as edges or non-edges 
# based on how their intensities are “connected”. 
# In this case, any gradient values below 30 are considered non-edges 
# whereas any values above 150 are considered edges.

canny = cv2.Canny(image, 30,150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

"""
Notice how the edges are more “crisp”. 
We have substantially less noise than when we used the 
Laplacian or Sobel gradient images. 

Furthermore, the outline of our coins are clearly revealed.

"""