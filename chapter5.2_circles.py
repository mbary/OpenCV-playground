import numpy as np
import sys
import cv2


# create a new drawing canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

# Calculate the the center of the 
# Bear in mind that it is counterintuitive so 
# the height of the image (y) is found in canvas.image[0]
# while the width of the image (x) is found in canvas.image[1]
# it is a common mistake to mix them up
(center_x, center_y) = (canvas.shape[1]//2, canvas.shape[0]//2)

# The colour white is max of all colours, while black is lack of all colours (0,0,0)
white = (255,255,255)

# we will create a bullseye, for that reason we loop in a number of radius ranges
for r in range(0,175,25):
    cv2.circle(canvas, (center_x,center_y), r, white)

cv2.imshow("Bullseye", canvas)
cv2.waitKey(0)

