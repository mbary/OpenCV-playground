import numpy as np
import cv2

"""
Now we will review four bitwise operations: AND, OR, XOR, and NOT. 
These four operations, while very basic and low level, are paramount to image processing, 
especially when we start working with masks in Section 6.4.

Bitwise operations operate in a binary manner and are represented as grayscale images. 
A given pixel is turned “off” if it has a value of zero, and it is turned “on” if the
pixel has a value greater than zero.
"""

rectangle = np.zeros((300,300), dtype = "uint8")

cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle = np.zeros((300,300), dtype = "uint8")
cv2.circle(circle, (150,150), 150,255,-1)
cv2.imshow("circle",circle)
cv2.waitKey(0)

bitwiseAND = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND", bitwiseAND)
cv2.waitKey(0)

bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOR)
cv2.waitKey(0)

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXOR)
cv2.waitKey(0)

bitwiseNOT = cv2.bitwise_not(rectangle, circle)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)


"""
As I mentioned above, a given pixel is turned “on” if it has a value greater than zero, 
and it is turned “off” if it has a value of zero. Bitwise functions operate on these binary conditions.

In order to utilize bitwise functions, we assume (in most cases) that we are comparing two pixels 
(the only exception is the NOT function). We’ll compare each of the pixels and then construct our bitwise representation.

Let’s quickly review our binary operations:

    1. AND: A bitwise AND is true if and only if both pixels are greater than zero.
    2. OR: A bitwise OR is true if either of the two pixels are greater than zero.
    3. XOR: A bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both.
    4. NOT:AbitwiseNOTinvertsthe“on”and“off”pixels in an image.
"""

