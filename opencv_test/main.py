import cv2
import barcode

code = barcode.Code128('rafael')
code = str(code.to_ascii())
print(code)
new_code = []
for letter in code:
    if letter == "X":
        letter = "1"
    else:
        letter = "0"
    new_code.append(letter)
new_code = ''.join(new_code)

print(new_code)


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
'''
def drawChar(opencv_image, char, position, bar_width, bar_height): 
    code128_codes = {"11010010000" : "11010010000",
    "11000111010" : "11000111010",
    "!" : "11001101100",
    '"' : "11001100110",
    "#" : "10010011000",
    "$" : "10010001100",
    "%" : "10001001100",
    "&" : "10011001000",
    "'" : "10011000100",
    "(" : "10001100100",
    ")" : "11001001000",
    "*" : "11001000100",
    "+" : "11000100100",
    "," : "10110011100",
    "-" : "10011011100",
    "." : "10011001110",
    "/" : "10111001100",
    "0" : "10011101100",
    "1" : "10011100110",
    "2" : "11001110010",
    "3" : "11001011100",
    "4" : "11001001110",
    "5" : "11011100100",
    "6" : "11001110100",
    "7" : "11101101110",
    "8" : "11101001100",
    "9" : "1110010110",
    ":" : "11100100110",
    ";" : "11101100100",
    "<" : "11100110100",
    "=" : "11100110010",
    ">" : "11011011000",
    "?" : "11011000110",
    "@" : "11000110110",
    "A" : "10100011000",
    "B" : "10001011000",
    "C" : "10001000110",
    "D" : "10110001000",
    "E" : "10001101000",
    "F" : "10001100010",
    "G" : "11010001000",
    "H" : "11000101000",
    "J" : "10110111000",
    "k" : "10110001110",
    "M" : "10111011000",
    "N" : "10111000110",
    "O" : "10001110110",
    "P" : "11101110110",
    "Q" : "11010001110",
    "R" : "11000101110",
    "S" : "11011101000",
    "T" : "11011100010",
    "V" : "11101011000",
    "C" : "11101000110",
    "x" : "11100010110",
    "W" : "11101000110",	
    "Y" : "11101101000",
    "Z" : "11101100010",
    "[" : "11100011010",
    "]" : "11001000010",
    "^" : "11110001010",
    "_" : "10100110000",
    "`" : "10100001100",
    "a" : "10010110000",
    "b" : "10010000110",
    "c" : "10000101100",
    "d" : "10000100110",
    "e" : "10110010000",
    "f" : "10110000100",
    "g" : "10011010000",
    "h" : "10011000010",
    "j" : "10000110010",
    "k" : "11000010010",
    "m" : "11110111010",
    "n" : "11000010100",
    "o" : "10001111010",
    "p" : "10100111100",
    "q" : "10010111100",
    "r" : "10010011110",
    "s" : "10111100100",
    "t" : "10011110100",
    "v" : "11110100100",
    "c" : "11110010100",
    "x" : "11110010010",
    "y" : "11011011110",
    "z" : "11011110110",
    "{" : "11110110110",
    "|" : "10101111000",
    "}" : "10100011110",
    "~" : "10001011110"}
    temp_start_code = '11010010000'
    temp_end_code = '11000111010'

    x_cursor = position[0]
    y_cursor = position[1]

    if char in code128_codes:
        char_code = code128_codes.get(char)
        for binary_number in char_code:
            if binary_number == '1':
                drawRect(opencv_image, (x_cursor, y_cursor), (x_cursor + bar_width, y_cursor + bar_height))
                x_cursor += bar_width
            if binary_number == '0':
                x_cursor += bar_width
'''
def drawBarcode(opencv_image, binary_info, position):

    bar_width = 3
    bar_height = 100
    
    x_cursor = 0

    for letter in binary_info:
        if letter == "1":
            drawRect(opencv_image, (position[0] + x_cursor, position[1]), (position[0] + bar_width, position[1] + bar_height))
        print(letter)
        x_cursor += bar_width


img = cv2.imread('opencv_test\images\example.png', 1)

pos = (10,10)

drawBarcode(img, new_code, pos)
#drawRect(img, (0,0), (100,100))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''bar_width = 3
bar_height = 50
start_pos = (50,50)
end_pos = (start_pos[0] + bar_width, start_pos[1] + bar_height)

drawRect(img, start_pos=start_pos, end_pos=end_pos)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''