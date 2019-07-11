import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

arg = str(sys.argv[1])
image = cv2.imread(arg)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Kept in BGR format
channels = cv2.split(image)
colours = ("b", "g", "r")

plt.figure()
plt.title("'Flattened', colour histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, colour) in zip(channels, colours):
    hist = cv2.calcHist([channel], [0], None, [256], [0,256])
    plt.plot(hist, color = colour)
    plt.xlim([0,256])
plt.show()


