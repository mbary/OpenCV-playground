import sys
import cv2
import numpy as np

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

"""
The first blurring method we are going to explore is averaging.

As the name suggests, we are going to define a k × k sliding window on top of our image, 
where k is always an odd number. 

This window is going to slide from left-to-right and from top-to-bottom. 
The pixel at the center of this matrix (we have to use an odd number, otherwise there would not be a true “center”) 
is then set to be the average of all other pixels surrounding it.

We call this sliding window a “convolution kernel” or just a “kernel”. 
We’ll continue to use this terminology throughout this chapter.
"""

blurred = np.hstack([cv2.blur(image, (3,3)),
                    cv2.blur(image,(5,5)),
                    cv2.blur(image,(7,7)),
                    cv2.blur(image,(15,15))])

cv2.imshow("Averaged method",blurred)
cv2.waitKey(0)


"""
Gaussian Blurring
"""
# Same as in the previous method we provide the image and a tuple representing the kernel size,
# however, we add a third argument which is our STD in the x-axis direction
# By setting this value to 0, we are instructing OpenCV to automatically compute them based on our kernel size. 
gausian = np.hstack([cv2.GaussianBlur(image, (3,3),0),
                     cv2.GaussianBlur(image, (5,5),0),
                     cv2.GaussianBlur(image, (7,7),0),
                     cv2.GaussianBlur(image, (15,15),0)])
cv2.imshow("Gaussian Methid", gausian)
cv2.waitKey(0)

"""
We can see the output of our Gaussian blur in Figure 8.3. 
Our images have less of a blur effect than when using the averaging method in Figure 8.2; 
however, the blur itself is more natural due to the computation of the weighted mean, rather 
than allowing all pixels in the kernel neighborhood to have equal weight.
"""


"""
Median
"""

"""
When applying a median blur, we first define our kernel size k. 
Then, as in the averaging blurring method, we consider all pixels in 
the neighborhood of size k × k. But, unlike the averaging method, instead of 
replacing the central pixel with the average of the neighborhood, we instead 
replace the central pixel with the median of the neighborhood.

Median blurring is more effective at removing salt-and- pepper style noise 
from an image because each central pixel is always replaced with a pixel intensity that exists in the image.

Averaging and Gaussian methods can compute means or weighted means for the 
neighborhood – this average pixel intensity may or may not be present in the neighborhood. 
But by definition, the median pixel must exist in our neigh- borhood. 
By replacing our central pixel with a median rather than an average, we can substantially reduce noise.

"""

median = np.hstack([cv2.medianBlur(image, 3),
                    cv2.medianBlur(image, 5),
                    cv2.medianBlur(image,7),
                    cv2.medianBlur(image,15)])
cv2.imshow("median blurring", median)
cv2.waitKey(0)


"""
Bilateral Blurring


Thus far, the intention of our blurring methods has been to reduce 
noise and detail in an image; however, we tend to lose edges in the image.


In order to reduce noise while still maintaining edges, we can use bilateral blurring. 
Bilateral blurring accomplishes this by introducing two Gaussian distributions.

The first Gaussian function only considers spatial neigh-bors, that is, pixels that 
appear close together in the (x, y) coordinate space of the image. 
The second Gaussian then models the pixel intensity of the neighborhood, ensuring 
that only pixels with similar intensity are included in the actual computation of the blur.

"""


# The first parameter we supply is the image we want to blur. 
# Then, we need to define the diameter of our pixel neighborhood. 
# The third argument is our color STD. A larger value for color STD means that 
# more colors in the neighborhood will be considered when computing the blur. 
# Finally, we need to supply the space STD. A larger value of space STD means that pixels farther 
# out from the central pixel will influence the blurring calculation, provided that their colors are similar enough.

bilateral = np.hstack([cv2.bilateralFilter(image, 5, 21,21),
                        cv2.bilateralFilter(image, 7,31,31),
                        cv2.bilateralFilter(image, 9,41,41),
                        cv2.bilateralFilter(image,13,73,73)])

cv2.imshow("Bilateral Blurring", bilateral)
cv2.waitKey(0)
