import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])
kernel_5x5 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, 2, -1, -1],
    [-1, 2, 4, 2, -1],
    [-1, -1, 2, -1, -1],
    [-1, -1, -1, -1, -1],
])

img = cv2.imread('C://Users//47463//Desktop//2//putao2.JPG', flags=cv2.IMREAD_GRAYSCALE)#以灰度形式加载图片
#使用模板矩阵进行高通滤波
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)
#使用OpenCV的高通滤波
GBlur = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - GBlur

cv2.imshow('img', img)
cv2.imshow('3x3', k3)
cv2.imshow('5x5', k5)
cv2.imshow('g_hpf', g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows()