import cv2
import barcode

def drawRect(opencv_image, start_pos, end_pos, color=(0,0,0)):
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
            opencv_image[row][column] = [color[0],color[1],color[2]]

def drawBarcode(opencv_image, info, position):
    code = barcode.Code128(info)
    code = str(code.to_ascii())
    new_code = []

    for letter in code:
        if letter == "X":
            letter = "1"
        else:
            letter = "0"
        new_code.append(letter)
    code = ''.join(new_code)

    bar_width = 3
    bar_height = 100

    x_cursor = position[0]
    y_cursor = position[1]

    for binary_number in code:
        if binary_number == '1':
            drawRect(opencv_image, (x_cursor, y_cursor), (x_cursor + bar_height, y_cursor + bar_width))
        y_cursor += bar_width

img = cv2.imread('opencv_test\images\example2.png', 1)

info = "30255"

drawBarcode(img, info, (200,10))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

