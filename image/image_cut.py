import cv2 as cv

img=cv.imread('C://Users//47463//Desktop//2//cat.jpg')
print('image_size:',img.shape)
img_cut=img[10:110,10:110]
print('image_size:',img_cut.shape)
cv.imwrite('img_cut.jpg',img_cut)
cv.namedWindow('img_cut',cv.WINDOW_AUTOSIZE)
cv.imshow('img_cut',img_cut)
cv.waitKey(0)
cv.destroyAllWindows()

