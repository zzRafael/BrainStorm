import cv2

def drawRect(opencv_image, start_pos, end_pos, color=(0,255,0)):
    # The positions has to have the arguments in (X, Y)
    # Check the start and end position.
    if start_pos[0] > end_pos[0] and start_pos[1] < end_pos[1]:
        real_start_pos = (end_pos[0], start_pos[1])
        real_end_pos = (start_pos[0], end_pos[1])
    if start_pos[0] > end_pos[0] and start_pos[1] > end_pos[1]:
        real_start_pos = end_pos
        real_end_pos = start_pos
    if start_pos[0] < end_pos[0] and start_pos[1] < end_pos[1]:
        real_start_pos = start_pos
        real_end_pos = end_pos
    if start_pos[0] < end_pos[0] and start_pos[1] > end_pos[1]:
        real_start_pos = (start_pos[0], end_pos[1])
        real_end_pos = (end_pos[0], start_pos[1])

    for row in range(real_start_pos[1], real_end_pos[1]):
        for column in range(real_start_pos[0], real_end_pos[0]):
            img[row][column] = [color[0],color[1],color[2]]

def drawNumbers(number):
    

img = cv2.imread('opencv_test\images\example.png', 1)

bar_width = 3
bar_height = 50
start_pos = (50,50)
end_pos = (start_pos[0] + bar_width, start_pos[1] + bar_height)

drawRect(img, start_pos=start_pos, end_pos=end_pos)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()