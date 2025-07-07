# resizing
import os

import cv2

image_paths= r'C:\Users\...'
img = cv2.imread(os.path.join(image_paths, 'birds.jpg'))

resized_img = cv2.resize(img, (640, 640))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
