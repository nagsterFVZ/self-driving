import cv2 as cv
import numpy as np
import sys
import time

img = cv.imread("../../capture.jpeg", 0)

if img is None:
    sys.exit("Could not read the image.")

start_time = time.time()

ret, binary = cv.threshold(img,160,255,cv.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(binary,kernel,iterations = 3)
dilation = cv.dilate(erosion,kernel,iterations = 5)
contours, hierarchy = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
largestArea = 0
largest = None
for contour in contours:
    area = cv.contourArea(contour) 
    if (area > largestArea):
        largestArea = area
        largest = [contour]

out = np.zeros((1080, 1920, 3), dtype = np.uint8)
cv.drawContours(out, largest, -1, color=(255, 255, 255), thickness=cv.FILLED)

print(f'Processing took {time.time() - start_time} seconds')

cv.imwrite("4 - final.jpeg", out)