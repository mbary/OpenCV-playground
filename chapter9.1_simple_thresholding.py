import sys
import cv2
import numpy as np


"""


Thresholding


Thresholding is the binarization of an image. 
In general, we seek to convert a grayscale image to a binary image, 
where the pixels are either 0 or 255.


A simple thresholding example would be selecting a pixel value p, 
and then setting all pixel intensities less than p to zero, 
and all pixel values greater than p to 255. In this way, 
we are able to create a binary representation of the image.

"""


"""

Simple Thresholding

Applying simple thresholding methods requires human intervention.
We must specify a threshold value T. All pixel intensities below T 
are set to 0. And all pixel intensities greater than T are set to 255.


We can also apply the inverse of this binarization by setting all 
pixels below T to 255 and all pixel intensities greater than T to 0.
"""
arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying Gaussian blurring helps re-move some of the 
# high frequency edges in the image that we are not concerned with.
blurred = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Blurred", blurred)

# cv2.threshold() method requires 4 arguments
# 1) A GrayScale image we wish to threshold
# 2) The threshold value (155)
# 3) The maximum value applied while thresholding (255)
# 4) The thresholding method. Using the cv2.thresh_binary() 
# which indicates that pixel value p greater than T are set to maximum (third argument)
(T, thresh) = cv2.threshold(blurred, 155,255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

# we apply inverse thresholding rather than normal thresholding by using cv2.THRESH_BINARY_INV 
# as our thresholding method. 
# As we can see, our coins are now white and the background is black. 
# This is convenient as we will see in the next example.
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("inverse threshold binary", threshInv)

# Remember, a mask only considers pixels in the original image where the mask is greater than zero. 
# Since our inverted thresholded image on Line 17 does a good job at approximating the 
# areas the coins are contained in, we can use this inverted thresholded image as our mask.
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)





