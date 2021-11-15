import numpy
from matplotlib import pyplot

def program2(filename):
    #width, height, maxval, grey values
    f = open(filename, "rb")
    width = int.from_bytes(f.read(2), byteorder="little", signed=False)
    height = int.from_bytes(f.read(2), byteorder="little", signed=False)
    maxVal = int.from_bytes(f.read(1), byteorder="little", signed=False)

    #create a matrix of size height and width
    imageMatrix = numpy.empty([int(height), int(width)], dtype=int)

    #populate the matrix
    ctr = 0
    widthCtr = 0
    heightCtr = 0
    while 1:
        byte = f.read(1)
        if byte == b"":
            break
        number = int.from_bytes(byte, byteorder="little", signed=False)
        imageMatrix[heightCtr][widthCtr] = number
        if widthCtr + 1 == int(width):
            widthCtr = 0
            heightCtr += 1
        else:
            widthCtr += 1

    #print the matrix if you want :)
    #pyplot.imshow(imageMatrix, pyplot.cm.gray)
    #pyplot.show()

    #get the new filename with _b.pgm
    index = filename.find("_b.pgm")
    outputFilename = filename[:index] + "_copy.pgm"

    #write the ints to the new file
    with open(outputFilename, 'wt') as file:
        file.write("P2\n")
        file.write(str(width))
        file.write(" ")
        file.write(str(height))
        file.write("\n")
        file.write(str(maxVal))
        file.write("\n")
        #write the image data
        for row in imageMatrix:
            for number in row:
                file.write(str(number) + " ")
            file.write("\n")