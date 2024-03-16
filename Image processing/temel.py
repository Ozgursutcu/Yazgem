
import cv2
import numpy as np
#image okuma
color_image = cv2.imread('image.png',cv2.IMREAD_COLOR)
gri_image = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
transparency = cv2.imread('image.png',cv2.IMREAD_UNCHANGED)
#image gösterme
cv2.imshow('Color', color_image)
cv2.imshow('Gray', gri_image)
cv2.imshow('Transparency', transparency)


#image kaydetme
#cv2.imwrite('color.png', color_image)
#cv2.imwrite('gray.png', gri_image)
#cv2.imwrite('transparency.png', transparency)

#görsel boyutları 
print(color_image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()