import cv2

def mark_image(image_path, coordinates):
  
    image = cv2.imread(image_path)
    
   
    x, y, width, height = coordinates
    
 
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    

    cv2.imshow("Marked Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "image.png"
coordinates = (100, 100, 200, 200)  # x, y, width, height
mark_image(image_path, coordinates)