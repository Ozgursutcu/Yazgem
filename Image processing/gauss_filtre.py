import cv2
import numpy as np

image = cv2.imread('noise_image.png')

gauss_filtered = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Gauss Filtered Image', gauss_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
