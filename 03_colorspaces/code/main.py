# Colorspaces
import os

import cv2

image_paths= r'C:\Users\...'
img = cv2.imread(os.path.join(image_paths, 'birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rgb', img_rgb)

cv2.waitKey(0)
