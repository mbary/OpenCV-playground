import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)

"""
Histogram equalization improves the contrast of an image by “stretching” the distribution of pixels. 
Consider a histogram with a large peak at the center of it. 
Applying histogram equalization will stretch the peak out towards the corner of the image, 
thus improving the global contrast of the image. 

Histogram equalization is applied to grayscale images.


This method is useful when an image contains foregrounds and backgrounds 
that are both dark or both light. 
It tends to produce unrealistic effects in photographs; however, it is normally 
useful when enhancing the contrast of medical or satellite images.

"""

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# equalizing function
eq = cv2.equalizeHist(gray)

cv2.imshow("Histogram Equalization", np.hstack([gray, eq]))
cv2.waitKey(0)