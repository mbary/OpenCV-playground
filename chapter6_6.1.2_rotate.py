import sys
import numpy as np
import cv2

arg = str(sys.argv[1])

image = cv2.imread(arg)
cv2.imshow("original", image)
cv2.waitKey(0)

(h,w) = image.shape[:2]

# While rotating, we have to specify the point we want to rotate around
# While most of the cases it will br around the center, it may be around any given point.
center = (w//2,h//2)

# Instead of manually creating a rotation matrix, we can call the getRotationMatrix2D function 
# The function takes in 3 arguments, the point around which we are rotating, the degrees (negative are to counter clockwise) and the scale
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# WarpAffine allows us to apply the matrix to the image
# It takes in the image we want to rotate, rotation matrix and the dimensions of our image
rotated = cv2.warpAffine(image, M, (h,w))
cv2.imshow("Rotated 45 degreea", rotated)
cv2.waitKey(0)

M1 = cv2.getRotationMatrix2D(center, -90, 1.4)

rotated1 = cv2.warpAffine(image,M1, (h,w))
cv2.imshow("Rotated -90 and scaled 1.4", rotated1)
cv2.waitKey(0)


def rotate(image, angle, center = None, scale = 1.0):
    (h,w) = (image.shape[1], image.shape[0])

    if center is None:
        center = (w//2,h//2)
    
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w,h))
    return rotated

rotated2 = rotate(image, -69,scale=.5)
cv2.imshow("Rotate Function", rotated2)
cv2.waitKey(0)


