import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('noise_image.png')

# Medyan filtre uygula
median_filtered = cv2.medianBlur(image, 5)

# Sonucu göster
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', median_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
