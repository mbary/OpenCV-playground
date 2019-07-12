"""


Adaptive Thresholding


One of the downsides of using simple thresholding methods is that we need to manually 
supply our threshold value T. 
Not only does finding a good value of T require a lot of manual experiments and parameter 
tunings, it’s not very helpful if the image exhibits a lot of range in pixel intensities.

Simply put, having just one value of T might not suffice.

In order to overcome this problem, we can use adaptive thresholding, which considers 
small neighbors of pixels and then finds an optimal threshold value T for each neighbor. 
This method allows us to handle cases where there may be dramatic ranges of pixel 
intensities and the optimal value of T may change for different parts of the image.

"""

import sys
import cv2
import numpy as np

arg = str(sys.argv[1])
image = cv2.imread(arg)
# cv2.imshow("Original",image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5,),0)
cv2.imshow("Gray", image)
cv2.imshow("Blurred", blurred)



# Again, first argument is the image we want to process,
# secondly we provide the maximum value

# The third argument is our method to COMPUTE the threshold for the current neighborhood of pixels. 
# By supplying cv2.ADAPTIVE_THRESH_MEAN_C, we indicate that we want to compute 
# the mean of the neighborhood of pixels and treat it as our T value.

# The fourth argument is our thresholding method. Again, the description of this parameter 
# is identical to the simple thresholding method mentioned above. 
# We use cv2.THRESH_BINAR Y_INV to indicate that any pixel intensity greater 
# than T in the neighborhood should be set to 255, otherwise it should be set to 0.

# the Fifth The next parameter is our neighborhood size. This integer value MUST BE ODD and 
# indicates how large our neighborhood of pixels is going to be. 
# We supply a value of 11, indicating that we are going to examine 11 × 11 pixel regions of the image, 
# instead of trying to threshold the image globally, as in simple thresholding methods.

# Finally, we supply a parameter simply called C. 
# This value is an integer that is subtracted from the mean, allowing 
# us to fine-tune our thresholding. We use C = 4 in this example.

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,4)
cv2.imshow("Adaptive Mean", thresh)



thresh1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15,3)
cv2.imshow("Gaussian Threshold",thresh1)
cv2.waitKey(0)


"""
In general, choosing between mean adaptive thresholding and Gaussian adaptive thresholding requires
a few ex- periments on your end. The most important parameters to vary are the neighborhood size 
and C, the value you subtract from the mean. By experimenting with this value, you will 
be able to dramatically change the results of your thresholding.

"""