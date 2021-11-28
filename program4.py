import numpy
from matplotlib import pyplot

def program4(filename):
    print(filename)

    f = open(filename, "rb")
    width = int.from_bytes(f.read(2), byteorder="little", signed=False)
    height = int.from_bytes(f.read(2), byteorder="little", signed=False)
    maxVal = int.from_bytes(f.read(1), byteorder="little", signed=False)
    kValue = int.from_bytes(f.read(1), byteorder="little", signed=False)

    print(width, height, maxVal, kValue)

    dataType = numpy.dtype(numpy.single)
    dataType = dataType.newbyteorder('<')

    #create a matrix of size height and width
    #populate U matrix
    U = numpy.zeros([int(height), int(kValue)], dtype=numpy.single)
    for heightIndex in range(height):
        for widthIndex in range(kValue):               
            workingNum = numpy.frombuffer(f.read(4), dtype=dataType, count=1)
            U[heightIndex][widthIndex] = workingNum

    #populate S Matrix
    S = numpy.zeros([int(kValue), int(kValue)], dtype=numpy.single)
    for kIndex in range(kValue):
        workingNum = numpy.frombuffer(f.read(4), dtype=dataType, count=1)
        S[kIndex][kIndex] = workingNum 

    #populate the VT matrix
    VT = numpy.zeros([int(kValue), int(width)], dtype=numpy.single)
    for kIndex in range(kValue):
        for widthIndex in range(width):
            workingNum = numpy.frombuffer(f.read(4), dtype=dataType, count=1)
            VT[kIndex][widthIndex] = workingNum
    V = VT.transpose()

    imageMatrix = U.dot(S).dot(VT)

    #print the matrix if you want :)
    #pyplot.imshow(imageMatrix, pyplot.cm.gray)
    #pyplot.show()

    #write the ints to the new file
    index = filename.find("_b.pgm.SVD")
    outputFilename = filename[:index] + "_k.pgm"

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
    