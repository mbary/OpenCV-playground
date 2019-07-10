import sys
import numpy as np
import cv2

"""
In order to draw a random circle we have to generate 3 values
The radius; the colour of the circle; and the pt (x,y) coordinate of where it is going to be drawn
"""
canvas = np.zeros((300,300,3), dtype="uint8")

# We will draw 25 circles

for i in range(0,25):
    radius = np.random.randint(5,high = 200)
    colour = np.random.randint(0,high =255, size=(3,)).tolist()
    pt = np.random.randint(0,high=300, size = (2,))
#   Last intiger is defines the thickess. A -1 ensures it is filled out
    cv2.circle(canvas, tuple(pt), radius, colour, -1)

cv2.imshow("Abstract", canvas)
cv2.waitKey(0)
