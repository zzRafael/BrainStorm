import cv2

class Barcode():
    def __init__(self, number2convert, width, height):

        self.number2convert = number2convert
        self.height = height
        self.width = width

        # define bars
        self.start_xpos = 50
        self.end_xpos = self.start_xpos + self.width
        self.start_ypos = 50
        self.end_ypos = self.start_ypos + self.height

        # convert the number to string
        self.number_string = str(self.number2convert)

        # open a file that cotains the barcode in binary code
        self.barcode_bin_codes = open('opencv_test\\barcodes_bin_codes.txt', "r")

        # get lines
        self.lines = self.barcode_bin_codes.readlines()


    def buildBarcode(self):
        # show the lines of the chars
        for char in self.number_string:
            for line in self.lines:
                if line.count(f'{char}=') == 1:
                    print(self.lines.index(line))

        for width_px in range(self.start_xpos, self.end_xpos):
            for height_px in range(self.start_ypos, self.end_ypos):
                self.img[height_px][width_px] = [0, 0, 0]

        # close the file that cotains the barcode in binary code
        self.barcode_bin_codes.close()


img = cv2.imread('opencv_test/images/example2.png')

Barcode(number2convert=123, width=10, height=200)


cv2.imshow('Image', img)
cv2.waitKey(0)
