import sys
import cv2
import numpy as np
"""
We all know basic arithmetic operations like addition and subtraction. 
But when working with images, we need to keep in mind the limits of our color space and data type.

For example, RGB images have pixels that fall within the range [0, 255]. 
So what happens if we are examining a pixel with intensity 250 and we try to add 10 to it?

Under normal arithmetic rules, we would end up with a value of 260. 
However, since RGB images are represented as 8-bit unsigned integers, 260 is not a valid value.

So, what should happen? Should we perform a check of some sort to ensure no pixel falls outside
the range of [0, 255], thus clipping all pixels to have a minimum value of 0 and a maximum value of 255?

Or do we apply a modulus operation, and “wrap around”? 
Under modulus rules, adding 10 to 250 would simply wrap around to a value of 4.

Which way is the “correct” way to handle image 
additions and subtractions that fall outside the range of [0, 255]?

The answer is there is no correct way – it simply depends on how you are 
manipulate your pixels and what you want the desired results to be.

However, be sure to keep in mind that there is a difference between 
OpenCV and NumPy addition. NumPy will perform modulo arithmetic and “wrap around”. 
OpenCV, on the other hand, will perform clipping and ensure pixel values never fall outside the range [0, 255].

"""

arg = str(sys.argv[1])

image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

print(f"Max of 255: {cv2.add(np.uint8([200]),np.uint8([100]))}")
print(f"Min of 0: {cv2.subtract(np.uint8([50]), np.uint8([100]))}")

print(f"Wrap Around: {np.uint8([200]) + np.uint8([100])}")
print(f"Wrap Around: {np.uint8([50]) - np.uint8([100])}")


# We define a NumPy array of ones, with the same size as our image. 

# Again, we are sure to use 8-bit unsigned integers as our data type. 
# In order to fill our matrix with values of 100’s rather than 1’s, we simply multiply our matrix of 1’s by 100. 
M = np.ones(image.shape, dtype="uint8")*100

# Finally, we use the cv2.add function to add our matrix of 100’s to the original image – 
# thus increasing every pixel intensity in the image by 100, but 
# ensuring all values are clipped to the range [0, 255] if they attempt to exceed 255.
added = cv2.add(image,M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M1 = np.ones(image.shape, dtype="uint8")*50
subtracted = cv2.subtract(image, M1)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)


"""
In this section, we explored the peculiarities of image arithmetic using OpenCV and NumPy. 
These caveats are important to keep in mind, otherwise you may get unwanted 
results when performing arithmetic operations on your images.
"""