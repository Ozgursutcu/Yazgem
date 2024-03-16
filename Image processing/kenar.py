import cv2

# Görüntüyü yükle
image = cv2.imread('image.png', 0)  # 0, görüntüyü gri tonlamalı olarak okur

# Canny kenar tespiti uygula
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Sonucu göster
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


