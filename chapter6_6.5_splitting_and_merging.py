import sys
import numpy as np
import cv2

"""
A color image consists of multiple channels: a Red, a Green, and a Blue component.
We have seen that we can access these components via indexing into NumPy arrays. 
But what if we wanted to split an image into its respective components?
"""

arg = str(sys.argv[1])

image = cv2.imread(arg)
# cv2.imshow("ORiginal", image)

# Bear in mind openCV interprets RGB as BGR
(B,G,R) = cv2.split(image)

cv2.imshow("Red Channel", R)
cv2.imshow("Green Channel", G)
cv2.imshow("Blue Channel", B)
cv2.waitKey(0)

# Merging the channels back together
merged = cv2.merge([B,G,R])
cv2.imshow("Merged channles", merged)
cv2.waitKey(0)

"""
An alternative method to visualize the channels of an image can be seen in Figure 6.12. 
In order to show the actual “color” of the channel, we first need to take apart the image
using cv2.split. Then, we need to reconstruct the image, but this time setting all pixels but the current channel as zero.
"""

# We construct a NumPy array of zeros, with the same width and height as our original image. 
zeros = np.zeros(image.shape[:2], dtype = "uint8")

# Then, in order to construct the Red channel representation of the image, we make a call 
# to cv2.merge, but specifying our zeros array for the Green and Blue channels.
cv2.imshow("Red Channel", cv2.merge([zeros,zeros,R]))
cv2.imshow("Green Channel", cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue Channel", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
