import cv2
import sys
import numpy as np

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)
"""
Using a mask allows us to focus only on the portions of the image that interests us.
"""

"""
we have an image of a beach. But I’m not interested in the beach in the image.
I’m only interested in the sky and the palm tree. 
We could apply a cropping to extract that region of the image. 
Or, we could apply a mask to the image.

The image on the Top-Right is our mask – a white rectangle at the center of the image. 
Applying our mask to our beach image, we arrive at the image on the Bottom. 
By using our rectangle mask, we have focused only on the sky and palm tree in the image.
"""

mask = np.zeros(image.shape[:2], dtype = "uint8")

# In order to draw the white rectangle, we first compute the center of the image 
# by dividing the width and height by two, using the // operator to indicate integer division.
(cx,cy) = (image.shape[1]//2, image.shape[0]//2)

# Drawing our aryan mask
cv2.rectangle(mask, (cx -75, cy - 75), (cx + 75, cy + 75), 255, -1)
cv2.imshow("Mask",mask)

# We apply the bitwise_AND function. It will include all pixles that are active.
# Obviously, the AND function will be True for all pixels in the image;
#  
# HOWEVER, the important part of this function is the mask keyword argument. 
# By supplying a mask, the cv2.bitwise_and function only examines pixels that are “on” in the mask. 
# In this case, only pixels that are part of the white rectangle.
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied", masked)
cv2.waitKey(0)

mask1 = np.zeros(image.shape[:2], dtype = "uint8")

cv2.circle(mask1, (cx,cy), 100, 255,-1)
cv2.imshow("Mask1", mask1)
cv2.waitKey(0)

masked1 = cv2.bitwise_and(image,image, mask=mask1)
cv2.imshow("Mask1 Applied", masked1)
cv2.waitKey(0)


"""
Again, the key point of masks is that they allow us to focus 
our computation only on regions of the image that interests us.
"""

