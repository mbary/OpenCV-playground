import sys
import numpy as np
import cv2

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("original", image)
"""
In this book, we have only explored the RGB color space; however, 
there are many other color spaces that we can uti- lize.

The Hue-Saturation-Value (HSV) color space is more similar to how humans think and conceive of color. 
Then there is the L*a*b* color space, which is more tuned to how hu- mans perceive color.

OpenCV provides support for many, many different color spaces. And understanding how color 
is perceived by humans and represented by computers occupies an entire li- brary of literature itself.

In order to not get bogged down in the details, I’ll just show you how to convert color spaces. 
If you think your application of image processing and computer vision might need a different color 
space than RGB, I will leave that as an exercise to the reader to explore the peculiarities of each color space.
"""

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
hsv1= cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
cv2.imshow("HSV Full", hsv1)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*A*B", lab)

lab1 = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("LAB - 0ther function", lab1)
cv2.waitKey(0)