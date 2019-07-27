"""


Contours



Previously, we explored how to detect edges in an image of coins.

Now we are going to use these edges to help us find the actual coins in the image and count them.

OpenCV provides methods to find “curves” in an image, called contours. 
A contour is a curve of points, with no gaps in the curve. 
Contours are extremely useful for such things as shape approximation and analysis.


In order to find contours in an image, you need to first obtain a binarization of the image, 
using either edge detection methods or thresholding. 
In the examples below, we’ll use the Canny edge detector to find the outlines of the coins, 
and then find the actual contours of the coins.

"""

import sys
import  numpy as np
import cv2

arg = str(sys.argv[1])
image = cv2.imread(arg)


# As in previous cases while edge detecting, we convert our image to grayscale 
# and apply the Gausisian Blur making it easier for the detectors to finr
# the outlines of the coins.

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11,11),0)
cv2.imshow("Original", image)


# We get the edges of the coins
# The gradients below 30, are considered non-edges, and above 150, are considered edges.
edged = cv2.Canny(blurred, 30,150)
cv2.imshow("Edges", edged)


"""
Now that we have the outlines of the coins, we can find rhe contours of the outlines.
We use the cv2.findContours function.
It returns a 2 or 3 tuple (depending on the vesrion), consisting of the image itself (which is modifief 
and essentially destroyed -- hence why we use a copy of the edged picture)
the countours themselves (cnts) and the hierarchy of contours 
"""

# the first argument is the edged image itself. It is important to use a copy of the image
# as the function destroyes the image it is given. If you intend on using it later on, it's best to make a copy
# We use the cv2.RETR_EXTERNAL to retrieve only the outermost contours (ones that follow the outline of the coin)

# (We can also pass in cv2.RETR_LIST to grab all contours. Other methods include 
# hierarchical contours using cv2.RETR_COMP and cv2.RETR_TREE, 
# but hierarchical contours are outside the scope of this book.)

# The last argument is how we want to approximate the contour. 
# We use cv2.CHAIN_APPROX_SIMPLE to compress horizontal, vertical, and 
# diagonal segments into their end- points only. 
# This saves both computation and memory. 
# 
# If we wanted all the points along the contour,
#  without compression, we can pass in cv2.CHAIN_APPROX_NONE; 
# however, be very sparing when using this function. Retrieving all 
# points along a contour is often unnecessary and is wasteful of resources.
(cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


print(f"I count {len(cnts)} coins in the image")

# We don't want to draw contours on our original image,
# hence wy we make a copy of it
coins = image.copy()

# cv2.drawContours actually draws the contours.
# first argument is the image on which the contours are to be drawn
#   Second argument is the list of contours detected earlier,
# By specifying the int -1, we indicate that we want all of the contours drawn 
# (any other int >0 would draw the respective contour)
#   The third argument is the colour in which we want the contours drawn, 
# Last argument is the thivkness of the contour line.
cv2.drawContours(coins, cnts, -1, (0,255,0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)


"""
Lets crop each individual coin from the image.

"""
for (i, c) in enumerate(cnts):
    # We use the cv2.boundingRect function on the current countour to find the "encolsing box"
    # that our contour will fit into, allowing us to crop it out of the image.
    # It takes a single paremeter, the countour.
    
    # It returns a tuple of the x y coordinates of the position where the rectangle starts, 
    # and the height and width of the rectangle 
    (x,y,w,h) = cv2.boundingRect(c)

    print(f"Coin #:{i+1}") 

    # We then crop the coin form the original image using the bounding coordinates
    # and np array slicing. 
    
    coin = image[y:y + h, x:x + w]

    cv2.imshow("a coin", coin)
    """
    If we can find the bounding box of a contour, why not fit a circle to the contour as well? 
    Coins are circles, after all.

    """
    # We firstly initialise a mask by as a np.array of zeros, with the same width and height 
    # as our original image. 
    mask = np.zeros(image.shape[:2], dtype="uint8")
    
    # cv2.minEnclosingCirle fits a circle to our contour, 
    # We pass in a circle variable, the current contour, and it returns 
    # the x,y coordinates of the center of the the circle, and its radius.

    ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)

    # Using the (x, y) coordinates and the radius, we can draw a circle on our mask, representing the coin.
    cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
    
    # We then crop the mask in the exact same manner as we cropped the coin
    mask = mask[y:y + h, x:x+w]

    
    # In order to show only the foreground of the coin and ig-nore the background, 
    # we make a call to our trusty bitwise AND function using the coin image and 
    # the mask for the coin. The coin, with the background removed
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)

    