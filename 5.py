import cv2 as cv
import numpy as np    
# Take two images for blending them together   
image1 = cv.imread("images/1.jpg", 0)
image2 = cv.imread("images/2.jpg", 0)
print(image1.shape)
print(image2.shape)
# Make the images of uniform size
img1 = cv.resize(image1, (400, 400))
img2 = cv.resize(image2, (400, 400))
print(img1.shape)
print(img1.shape)

# Make sure images got an alpha channel
res = cv.addWeighted(img1, 0.3, img2, 0.7, 0.0)

result = np.zeros((400, 400*4), dtype='uint8')

merge1 = img1//2 + img2//4
merge2 = img1//4 + img2//2
print(result.shape)
result[0:400, 0:400]=img1
result[0:400, 400:400*2]=merge1
result[0:400, 400*2:400*3]=merge2
result[0:400, 400*3:400*4]=img2


# Display the images
cv.imwrite('result_5.jpg', result)
#cv.imshow('output', res)
cv.waitKey()
