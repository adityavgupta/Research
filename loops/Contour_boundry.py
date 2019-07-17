import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('r_loop.png')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
red = rgb_img[:, :, 0]
height, width, channels = rgb_img.shape

#create mask and flood fill
mask = np.zeros((height+2, width+2), np.uint8)
flooded = red.copy()
flags = 4 | cv2.FLOODFILL_MASK_ONLY
cv2.floodFill(flooded, mask, (8, 8), 1, 2, 2, flags)

#some cleanup
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
omask = cv2.morphologyEx(1-mask, cv2.MORPH_OPEN, kernel)
#plt.imshow(omask)
#plt.colorbar()
plt.show()

#find contours
contours, hierarchy = cv2.findContours(omask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

#find largest area contour
largest_contour = []
largest_area = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > largest_area:
        largest_area = area
        largest_contour = contour

x,y,w,h = cv2.boundingRect(largest_contour)
cv2.drawContours(rgb_img, [largest_contour], -1, (0, 128, 128), 1)
cv2.rectangle(rgb_img, (x,y), (x+w, y+h), (128, 0, 0), 1)
plt.imshow(rgb_img)
plt.show()