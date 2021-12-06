import numpy
from matplotlib import pyplot
import re
from scipy.linalg import svd

def program3(filename, kValue):
    #open file and read text,
    with open(filename, 'rt') as f:
        buffer = f.read()
    try:
        #get header, width, height, and maxval
        header, width, height, maxval = re.search(
            "(^P2\s(?:\s*#.*[\r\n])*"
            "(\d+)\s(?:\s*#.*[\r\n])*"
            "(\d+)\s(?:\s*#.*[\r\n])*"
            "(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        #file format doesn't work correctly (probably an extra space somewhere)
        raise ValueError("Not a raw PGM file: '%s'" % filename)

    f = open(filename, 'r')
    Lines = f.readlines()

    #create a matrix of size height and width
    imageMatrix = numpy.empty([int(height), int(width)], dtype=int)

    #populate the matrix
    ctr = 0
    widthCtr = 0
    heightCtr = 0
    for line in Lines:
        #skip comments
        if line[0] == '#':
            continue
        #skip first 3 lines
        if ctr < 3:
            ctr += 1
            continue
        #populate the matrix with values
        for number in line.split() :
            imageMatrix[heightCtr][widthCtr] = number
            if widthCtr + 1 == int(width):
                widthCtr = 0
                heightCtr += 1
            else:
                widthCtr += 1
    
    #print the matrix if you want :)
    #pyplot.imshow(imageMatrix, pyplot.cm.gray)
    #pyplot.show()

    #SVD
    U, S, VT = svd(imageMatrix, full_matrices=True)

    kValue = int(kValue)
    valueCtr = 0
    totalValue = 0
    for value in S:
        totalValue += value
        valueCtr += 1
    if valueCtr < kValue:
        print("ERROR: kValue CANNOT BE GREATOR THAN THE AMOUNT OF VALUES IN SVD")
        exit(1)
    
    kValueCtr = 1
    totalPercentageValue = 0
    for value in S:
        if kValueCtr > kValue:
            break
        totalPercentageValue += value / totalValue
        kValueCtr += 1
    
    totalPercentageValue *= 100
    print("Compressing with K value of: ", kValue ," with ", totalPercentageValue, "% Compression rate")

    index = filename.find(".pgm")
    outputFilename = filename[:index] + "_b.pgm.SVD"

    #write the bytes to the new file
    with open(outputFilename, 'wb') as file:
        # 2 bytes for width and height
        file.write((int(width)).to_bytes(2, byteorder='little', signed=False))
        file.write((int(height)).to_bytes(2, byteorder='little', signed=False))
        file.write((int(maxval)).to_bytes(1, byteorder='little', signed=False))
        file.write(int(kValue).to_bytes(1, byteorder='little', signed=False))
        #write U matrix
        for row in U[:,:kValue]:
            for number in row:
                numberSingle = number.astype(numpy.single)
                numberByte = numberSingle.tobytes(order = 'C')
                file.write(numberByte)
        #write S array
        for number in S[:kValue]:
            numberSingle = number.astype(numpy.single)
            numberByte = numberSingle.tobytes(order = 'C')
            file.write(numberByte)
        #write V Matrix
        for row in VT[:kValue]:
            for number in row:
                numberSingle = number.astype(numpy.single)
                numberByte = numberSingle.tobytes(order = 'C')
                file.write(numberByte)

    outputFilename.close()

    print("Success")
        