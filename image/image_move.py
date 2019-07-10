import cv2
import numpy as np

image = cv2.imread('C://Users//47463//Desktop//2//cat.jpg')
M = np.float32([[1, 0, 10], [0, 1, 10]])
moveImage = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.namedWindow('move',cv2.WINDOW_NORMAL)
cv2.imshow('move', moveImage)
cv2.waitKey()
cv2.destroyAllWindows()
