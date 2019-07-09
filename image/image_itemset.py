import cv2

img = cv2.imread('C://Users//47463//Desktop//2//cat.jpg')
print("shape : ", img.shape)

print("pixel (10, 10) B value", img.item(10, 10, 0))
img.itemset((10, 10, 0), 255)
print("pixel (10, 10) B value", img.item(10, 10, 0))

print("pixel (20, 20) G value", img.item(20, 20, 1))
img.itemset((20, 20, 1), 255)
print("pixel (20, 20) G value", img.item(20, 20, 1))

print("pixel (30, 30) R value", img.item(30, 30, 2))
img.itemset((30, 30, 2), 255)
print("pixel (30, 30) R value", img.item(30, 30, 2))

cv2.namedWindow('itemset',cv2.WINDOW_AUTOSIZE)
cv2.imshow('itemset',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
