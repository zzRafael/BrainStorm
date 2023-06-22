import cv2

img = cv2.imread('opencv_test/images/example.png')

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [0,0,0]

cv2.imshow('Image', img)
cv2.waitKey(0)
