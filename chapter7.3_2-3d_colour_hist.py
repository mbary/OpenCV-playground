import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np


"""
Up until this point, we have computed a histogram for only one channel at a time. 
Now we move on to multidimensional histograms and take into consideration two channels at a time.


For example, we can ask a question such as, 
“How many pixels have a Red value of 10 AND a Blue value of 30?”. 
How many pixels have a Green value of 200 AND a Red value of 130? 

By using the conjunctive AND, we are able to construct multi-dimensional histograms.
"""

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("original", image)
cv2.waitKey(0)

channels = cv2.split(image)
colours = ("b", "g", "r")

fig = plt.figure()

ax = fig.add_subplot(131)

hist = cv2.calcHist([channels[1],channels[0]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Colour Hist of G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)

hist = cv2.calcHist([channels[1], channels[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Colour Hist of G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)

hist = cv2.calcHist([channels[2],channels[0]], [0,1],None ,[32,32], [0,256,0,256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Colour Hist of B and R")
plt.colorbar(p)

print(f"2D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values.")

plt.show()


hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
plt.plot(hist)
print(f"3D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values.")
plt.show()