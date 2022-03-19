import cv2 as cv

def change(val):
    print(val)
    a = val/100
    b = (1.0 - a)
    result = cv.addWeighted(img1, a, img2, b, 0.0)
    cv.imshow('melange', result)
 
 
img1 = cv.imread('images/1.jpg')
img2 = cv.imread('images/2.jpg')
 
img1 = cv.resize(img1, (400, 400))
img2 = cv.resize(img2, (400, 400))
 
cv.imshow('melange', img2)
 
cv.createTrackbar('slider', 'melange', 0, 100, change)
 
cv.waitKey(0)
cv.destroyAllWindows()