import sys
import numpy as np
import cv2

arg = str(sys.argv[1])

image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

# We flip an image using the cv2.flip() function.
# First argument is the image, second is an integer

# 1 means flip horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Holizontally", flipped)
cv2.waitKey(0)

# 0 means flip vertically
flipped2 = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped2)
cv2.waitKey(0)

# a negative value means flip both vertically and horizontally
flipped3 = cv2.flip(image, -1)
cv2.imshow("Flipped Both Horizontally and Vertically", flipped3)
cv2.waitKey(0)

