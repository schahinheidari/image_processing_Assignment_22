import cv2 as cv


img1 = cv.imread("images/a.tif", 0)
img2 = cv.imread("images/b.tif", 0)


for i in range(512):
    for j in range(512):
        img1[i,j] = 255 - img1[i,j]
        img2[i,j] = 255 - img2[i,j]
res = img1 - img2
res = cv.subtract(img1, img2)
print(res.shape)
cv.imwrite('images/decrypt.jpg', res)
cv.imshow('output', res)
cv.waitKey()