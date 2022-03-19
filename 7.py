import cv2 as cv
import numpy as np
# Let's first create a zero image with the same dimensions of the loaded image
img = cv.imread("images/Mona_Lisa.jpg")
img = cv.resize(img,(400, 400))

# Generate Gaussian noise
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
# Add the Gaussian noise to the image
imggauss = cv.add(img,gauss)
# Display the image
cv.imwrite("result7.jpg", imggauss)
cv.imshow('a',imggauss)
cv.waitKey(0)
