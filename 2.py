import cv2 as cv
import numpy as np
import glob

images = []

for address in glob.glob("/home/shahin/Desktop/Sajjad project/Assignment-22/image_processing_Assignment_22/images/black_hole/**/*"):
    img = cv.imread(address)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    images.append(img)

res = np.zeros((2000, 2000), dtype="uint8")
print(res)

image_without_noise = [0 for i in range(4)]

for i in range(4):
    for j in range(5):
        image_without_noise[i] = image_without_noise[i] + (images[i][j] / 5)

final_image = np.zeros((2000, 2000), dtype=np.uint8)

image_without_noise=np.uint8(image_without_noise)

#print(image_without_noise)


#cv.imshow('Final Image', image_without_noise)

#cv.imwrite('final_image.jpg', image_without_noise)

#cv.waitKey()



