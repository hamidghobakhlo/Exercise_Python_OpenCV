# crop
import os

import cv2

image_paths= r'C:\Users\...
img = cv2.imread(os.path.join(image_paths, 'bird.jpg'))

print(img.shape)

cropped_img = img[220:740, 320:940]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
