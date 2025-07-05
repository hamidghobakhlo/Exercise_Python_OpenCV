import os

import cv2

# read image
image_paths= r'C:\Users\hamid\murph_env\project\Exercise_Python_OpenCV\pictures'
image_path = os.path.join(image_paths, 'bird.jpg')

img = cv2.imread(image_path)

# write image
image_output_path = r'C:\Users\hamid\murph_env\project\Exercise_Python_OpenCV\01_io'
cv2.imwrite(os.path.join(image_output_path, 'bird_out.jpg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(0)
