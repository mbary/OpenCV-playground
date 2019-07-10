import numpy as np
import cv2

"""
Up until this point, we have only loaded images off disk.
However, we can also define our images manually using Numpy arrays
Given that OpenCV interprets an image as a NumPy array, there is no reason 
why we can’t manually define the image ourselves!

# Initialise our image.
# 300x300 pixels and we allocate 3 channels - one for Red, Green, Blue respectively 
"""

canvas = np.zeros((300,300,3), dtype= "uint8")

"""
It’s important to draw your attention to the second argu- ment of the np.zeros method: the data type, dtype. 
Since we are representing our image as an RGB image with pixels in the range [0, 255], it’s important that 
we use an 8-bit un- signed integer, or uint8.
"""

# Now when we've initialised our canvas we can start drawing

# definte the tuple used to represent te colour green
green = (0, 255, 0)

# We now draw a line from point (0,0) - top left corner,  to the point (300,300) - bottom right corner
# First argument specifies the image we're going to draw on, second and third are the start and end point respectivly
# the last argument is the colour. 
cv2.line(canvas,(0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


red = (0,0,255)
# In the code below, the last argument (3) controls the thickness of the line.
# The argument specifies the thickness in pixels, in this case 3 pixels.
cv2.line(canvas, (300,0), (0,300), red,3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

"""
Drawing Rectangles
"""
# Similariy as with lines, first argument specifies the image to draw on,
# second and third arguments specify start and end coordinates and last argument the colour
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

# In the same manner we specify the thickness of hte line
cv2.rectangle(canvas, (50,200), (200,225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)

# By specifing the thinckess as -1, we draw a FILLED IN, rectangle as solid blue.
cv2.rectangle(canvas, (200,50), (225,125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


