import os

import cv2

# read image
image_paths= r'C:\Users\hamid\murph_env\project\Exercise_Python_OpenCV\pictures'
image_path = os.path.join(image_paths, 'bird.jpg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(0)
