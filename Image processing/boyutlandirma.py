import cv2

image = cv2.imread('image.png')

width = 300
height = 200

resized = cv2.resize(image, (width, height))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
