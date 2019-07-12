"""


otsu and riddler-calvard


Another way we can automatically compute the 
threshold value of T is to use Otsu’s method.

Otsu’s method assumes there are two peaks in the grayscale histogram of the image. 
It then tries to find an optimal value to separate these two peaks – thus our value of T.

While OpenCV provides support for Otsu’s method, I prefer the implementation 
by Luis Pedro Coelho in the mahotas package since it is more Pythonic.

"""

import sys
import cv2
import numpy as np
import mahotas

arg =str(sys.argv[1])
image = cv2.imread(arg)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Image", image)

# To compute our optimal value of T, we use the otsu function in the mahotas.thresholding package.
T = mahotas.thresholding.otsu(blurred)
print(f"Otsu's threshold: {T}")


thresh = image.copy()
thresh[thresh>T] = 255

thresh[thresh<255] = 0

thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu",thresh)


# We will now compute T using the Riddler-Calvard Method
T = mahotas.thresholding.rc(blurred)
print(f"Riddlee-Calvard threshold: {T}")

thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<255] = 0

thresh = cv2.bitwise_not(thresh)

cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
