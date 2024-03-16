import cv2
import numpy as np

image = cv2.imread("image.png")

x = 100
y = 100
width = 200
height = 150

cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
cv2.imshow("Dortgenli Gorsel", image)
#----------------------------------------------------------------  

points = [(150, 100), (250, 100), (200, 200)]

cv2.polylines(image, [np.array(points)], True, (0, 0, 255), 2)
cv2.imshow("Poligonlu Gorsel", image)
#----------------------------------------------------------------   
center = (300, 200)
radius = 50
color = (255, 0, 0)
thickness = 2

cv2.circle(image, center, radius, color, thickness)
cv2.imshow("Çemberli Gorsel", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

