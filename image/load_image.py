import cv2 as cv
src=cv.imread('C://Users//47463//Desktop//2//cat.jpg',flags=cv.IMREAD_GRAYSCALE)
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()
