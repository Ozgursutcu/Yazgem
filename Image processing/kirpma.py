import cv2

image = cv2.imread('image.png')

# Kırpılacak bölgenin koordinatları: startY:endY, startX:endX
cropped = image[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
