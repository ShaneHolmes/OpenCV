import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('test_camera')
success, frame = cameraCapture.read()
while success:
    if cv2.waitKey(1000) == 27:#Esc的ASCII码为27
        break
    cv2.imshow('test_camera', frame)
    success, frame = cameraCapture.read()

cv2.destroyAllWindows()
cameraCapture.release()
