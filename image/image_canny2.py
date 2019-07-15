import cv2

img = cv2.imread("C://Users//47463//Desktop//2//car.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gauss = cv2.GaussianBlur(gray, (3, 3), 1)

def doCanny(x):
    position = cv2.getTrackbarPos("CannyBar", "Canny")
    canny = cv2.Canny(gauss, position, position*2.5)
    cv2.imshow("Canny", canny)


cv2.namedWindow("Canny")

cv2.createTrackbar("CannyBar", "Canny", 1, 100, doCanny)

cv2.waitKey(0)