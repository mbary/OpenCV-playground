import sys
import numpy as np
import cv2

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

"""
Unsurprisingly we will be using cv2.resize function.
HOWEVER it is key that we have to keep in mind the ASPECT RATIO of the image in order to avoid distortion.
The aspect ratio is the proportional relationship of the width and the height of the image.
"""

# Computing the Aspect Ratio of the new image.

# We define our new image width to be 150 pixels.
# In order to compute the ratio of the new height to the old height, 
# we simply define our ratio r to be the new width (150 pixels) divided 
# by the old width, which we ac- cess using image.shape[1].
r = 150 / image.shape[1]

# Now that we have our ratio, we can compute the new dimensions of the image. 
# Again, the width of the new image will be 150 pixels. 
# The height is then computed by multiplying the old height by our ratio
dim = (150, int(image.shape[0] * r))

# Resizing of the image.
# The first argument is the image we wish to resize and the second is our computed dimensions for the new image.
# The last parameter is our interpolation method, which is the algorithm working behind the scenes to handle how the actual image is resized. 
# In general, I find that using cv2.INTER_AREA obtains the best results when resizing; 
# however, other appropriate choices include cv2.INTER_LINEAR, cv2.INTER_CUBIC, and cv2.INTER_NEAREST.
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
resized2 = cv2.resize(image, dim, interpolation = cv2.INTER_LINEAR)
cv2.imshow("Resized Width", resized)
cv2.waitKey(0)

cv2.imshow("Inter_linear resize", resized2)
cv2.waitKey(0)

"""
In the example we just explored, we only resized the image by specifying the width. 
But what if we wanted to resize the image by specifying the height? 
All that requires is a change to computing the aspect ratio:
"""

r1 = 50 / image.shape[0]
dim1 = (int(image.shape[1]*r1), 50)
resized3 = cv2.resize(image, dim1, interpolation = cv2.INTER_AREA)

cv2.imshow("Resized width", resized3)
cv2.waitKey(0)


def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

resized4 = resize(image, height=200)
cv2.imshow("resize function by height",resized4)
cv2.waitKey(0)

