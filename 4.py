import cv2 as cv

images = []
for i in range(15):
    img = cv.imread(f"images/highway/h{i}.jpg", 0)
    images.append(img)
    rows, cols = img.shape

res = np.zeros((rows, cols), dtype="uint8")
#print(res.shape)
for image in images:
    res += image//14

res = cv.resize(res,(400,400))
cv.imwrite("result4.jpg", res)
cv.imshow('output', res)
cv.waitKey()