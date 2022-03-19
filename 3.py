import cv2 as cv
import numpy as np


img1 = cv.imread("images/board - origin.bmp", 0)
img2 = cv.imread("images/board - test.bmp", 0)

img2 = cv.flip(img2,1)
res = cv.absdiff(img2,img1)
#res = cv.subtract(img2,img1)
res = cv.resize(res ,(500,500))

cv.imwrite('images/result3.jpg', res)
cv.imshow("different board",res)
cv.waitKey()