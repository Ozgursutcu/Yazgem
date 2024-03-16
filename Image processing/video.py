import cv2
video = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
kayit = cv2.VideoWriter('kayit.mp4', codec, 20.0, (640, 480))

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    kayit.write(frame)
    
    cv2.imshow('Live Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
kayit.release()
cv2.destroyAllWindows()

