import cv2

img = cv2.imread('opencv_test\images\example.png', -1)


img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('opencv_test\images\new_img.png', img)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()