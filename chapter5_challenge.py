import numpy as np
import cv2

canvas = np.zeros((300,300,3), dtype="uint8")
(center_x, center_y) = (canvas.shape[1]//2, canvas.shape[0]//2)


# rectangles
for (row, y) in enumerate(range(0,300,10)):
    for (col, x) in enumerate(range(0,300,10)):
        colour = (0,0,255)

        if row % 2 == col % 2:
            colour = (0,0,0)

        cv2.rectangle(canvas, (x,y), (x + 10, y + 10), colour, -1)

# green cicrle in the center
green = (0,255,0)
cv2.circle(canvas, (center_x,center_y), 50, green, -1)

cv2.imshow("Challenge", canvas)
cv2.waitKey(0)
