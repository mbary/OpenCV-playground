import sys
import numpy as np
import cv2


"""
This chapter is primarily concerned with gradients and edge detection. 
Formally, edge detection embodies mathematical methods to find points 
in an image where the brightness of pixel intensities changes distinctly.


The first thing we are going to do is find the “gradient” of the grayscale image, 
allowing us to find edge-like regions in the x and y direction.


We’ll then apply Canny edge detection, a multi-stage process of noise reduction (blurring), 
finding the gradient of the image (utilizing the Sobel kernel in both the horizontal and vertical direction), 
non-maximum suppression, and hysteresis thresholding.
"""

arg = str(sys.argv[1])
image = cv2.imread(arg)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)


# When computing gradients and edges, we (normally) compute them on a single channel – in this case, 
# we are using the grayscale image; however, we can also compute gradients for each channel of the RGB image. 

# For the sake of simplicity, let’s stick with the grayscale image since that is what you will use in most cases.

# We use the Laplacian method to compute the gradient magnitude image by calling the cv2.Laplacian function. 
# The first argument is our grayscale image – the image we want to compute the gradient magnitude 
# representation for. 
# The second argument is our data type for the output image.

# Throughout this book, we have mainly used 8-bit un- signed integers. Why are we using a 64-bit float now?
# The reason involves the transition of black-to-white and white-to-black in the image.

# The short answer here is that if you don’t use a floating point data type when computing 
# the gradient magnitude image, you will miss edges, specifically the white-to-black transitions.

lap = cv2.Laplacian(image, cv2.CV_64F)

# In order to ensure you catch all edges, use a floating point data type, 
# then take the absolute value of the gradient im-age and convert it back to an 8-bit 
# unsigned integer. 
# This is definitely an important technique to take note of – otherwise you’ll be missing edges in your image!
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian", lap)
cv2.waitKey(0)



"""


Sobel Gradient Representation


"""
# Using the Sobel operator, we can compute gradient magnitude
#  representations along the x and y axis, allowing us
# to find both horizontal and vertical edge-like regions.

# The first argument is the image we want to compute the gradient representation for.
# Then, just like in the Laplacian example above, we use a floating point data type. 
# The last two arguments are the order of the derivatives in the x and y direction, respectively. 
# Specify a value of 1 and 0 to find vertical edge-like regions and 0 and 1 to find horizontal edge-like regions

sobelX = cv2.Sobel(image, cv2.CV_64F, 1,0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0,1)

# then ensure we find all edges by taking the absolute value of the floating point 
# image and then converting it to an 8-bit unsigned integer.
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# In order to combine the gradient images in both the x and y direction, we can apply a bitwise OR. 
# Remember, an OR operation is true when either pixel is greater than zero. 
# Therefore, a given pixel will be True if either a horizontal or vertical edge is present.


sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("SobelX", sobelX)
cv2.imshow("SobelY", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)


"""
One thing you’ll notice is that the edges are very “noisy”. 
They are not clean and crisp. We’ll remedy that by using
the Canny edge detector in the next section.
"""