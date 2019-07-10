import cv2

img = cv2.imread('C://Users//47463//Desktop//2//cat.jpg')
print(img.shape[:2])

height, width = img.shape[:2]

reSize1 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
reSize2 = cv2.resize(img, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)

cv2.imshow('reSize1', reSize1)
cv2.imshow('reSize2', reSize2)

cv2.waitKey()
cv2.destroyAllWindows()
