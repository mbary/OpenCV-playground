import sys
import cv2
import matplotlib.pyplot as plt


arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)


"""
  HISTOGRAMS
"""

"""
When plotting the histogram, the X-axis serves as our “bins”. 
If we construct a histogram with 256 bins, then we are effectively counting 
the number of times each pixel value occurs. 

In contrast, if we use only 2 (equally spaced) bins, then we are counting the 
number of times a pixel is in the range [0, 128) or [128, 255]. 
The number of pixels binned to the x-axis value is then plotted on the y-axis.


By simply examining the histogram of an image, you get a general 
understanding regarding the contrast, brightness, and intensity distribution.
"""

# We will be using the cv2.calcHist function to build our histograms.

# cv2.calcHist(images,channels,mask,histSize,ranges)

"""
1. images: This is the image that we want to compute a histogram for. Wrap it as a list: [myImage].

2. channels: This is a list of indexes, where we specify the index of the channel we want to compute a histogram for. 
    To compute a histogram of a grayscale image, the list would be [0]. 
    To compute a histogram for all three red, green, and blue channels, the chan- nels list would be [0,1,2].

3. mask: Remember learning about masks in Chapter 6? Well, here we can supply a mask. 
    If a mask is provided, a histogram will be computed for masked pixels only. 
    If we do not have a mask or do not want to apply one, we can just provide a value of None.

4. histSize: This is the number of bins we want to use when computing a histogram. 
    Again, this is a list, one for each channel we are computing a histogram for. 
    The bin sizes do not all have to be the same. 
    Here is an example of 32 bins for each channel: [32,32,32].

5. ranges: Here we specify The range of possible pixel values. 
    Normally, this is [0, 256] for each channel, but if you are using a color 
    space other than RGB (such as HSV), the ranges might be different.
"""



"""
grayscale histograms
"""

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale", gray)
cv2.waitKey(0)


hist = cv2.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)