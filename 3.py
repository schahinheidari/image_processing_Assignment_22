import cv2 as cv

img1 = cv.imread("images/board - origin.bmp", 0)
img2 = cv.imread("images/board - test.bmp", 0)

#img2 = cv.flip(img2,1)


img2 = img2[:,::-1]
# rotate all of columns
'''
matrix = [
[0, 1, 2],
[3, 4, 5],
[6, 7, 8]
]
after rotate :
matrix = [
[2, 1, 0],
[5, 4, 3],
[8, 7, 6]
]
'''
res = cv.absdiff(img2,img1)
#res = cv.subtract(img2,img1)
res = cv.resize(res ,(400,400))

#cv.imwrite('images/result3.jpg', res)
cv.imshow("different board",res)
cv.waitKey()