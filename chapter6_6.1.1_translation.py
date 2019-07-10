import numpy as np
import cv2
import sys
# iThis isn’t a package included in NumPy or OpenCV. 
# Rather, it’s a library that we are going to write ourselves and create “convenience” 
# methods to do common tasks like translation, rotation, and resizing.
import imutils


"""
Chapter 6 talks about Simple Image Processing techinques
"""

"""
6.1

Covering Basic Image transformations
Such as translation, rotation, resizing, flipping and cropping.

They are important in nearly all areasd of Computer Vision

"""

"""
6.1.1

Translation 
Shifting an image image along the x,y axis 
"""

arg = str(sys.argv[1])

image = cv2.imread(arg)
cv2.imshow("Original", image)

cv2.waitKey(0)

# The translation of an image begins by defining our translation Matrix M
# The Matrix tells us how many pixels an image is to be shifted by.
# Our translation matrix M is defined as a floating point array – this is important because OpenCV expects this 
# matrix to be of floating point type. 

# The first row of the matrix is [1,0,tx], where tx is the number of pixels we will shift the image left or right. 
# Negative values of tx will shift the image to the left and positive values will shift the image to the right.

# Then, we define the second row of the matrix as [0, 1, ty ], where ty is the number of pixels we will shift the image up or down. 
# Negative value of ty will shift the image up and positive values will shift the image down.

M = np.float32([[1,0,25], [0,1,50]])

# The Actual translation takes place using the cv2.warpAffine function
# The arguments are, our image, Translation Matrix and the dimensions of our image.
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Shifted down and right", shifted)
cv2.waitKey(0)


M1 = np.float32([[1,0,-50],[0,1,-90]])
shifted1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted1)
cv2.waitKey(0)


def translate(image, x, y):
    M = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

shifted2 =  translate(image, 100,40)
cv2.imshow("Function Translation", shifted2)
cv2.waitKey(0)

