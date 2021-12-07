import sys
import re
import os
import numpy
import matplotlib.pyplot as plt

from program3 import program3
from program4 import program4

#size of original image.ascii
filename = sys.argv[1]

index = filename.find('.pgm')
kFilename = filename[:index] + "_k.pgm"

index = filename.find(".pgm")
program4Filename = filename[:index] + "_b.pgm.SVD"

def getImageMatrix(filename):
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
    imageMatrix = numpy.empty([int(height), int(width)], dtype=numpy.single)

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
    
    return imageMatrix

#file1 is the main file, file2 is the secondary file
#imputs 2 pgm files
def findPercentError(file1, file2):
    print("RUNING PERCENT ERROR")
    f1Matrix = getImageMatrix(file1)
    f2Matrix = getImageMatrix(file2)

    shape = f1Matrix.shape
    height = shape[0]
    width = shape[1]

    print(height, width)

    workingPercentage = 0
    workingNum = 0
    for heightIndex in range(height):
        for widthIndex in range(width):
            workingNum = f1Matrix[heightIndex][widthIndex] - f2Matrix[heightIndex][widthIndex]
            if workingNum < 0:
                workingNum *= -1
            workingPercentage =+ workingNum / f1Matrix[heightIndex][widthIndex]

    return workingPercentage / (height * width)

y =  numpy.zeros([254])

for kValue in range(1,255):
    program3(filename, kValue)
    program4(program4Filename)
    y[kValue - 1] = findPercentError(filename, kFilename)

x = numpy.arange(1, 255)

# plotting
plt.title("Compression Rate bytes (CAS.pgm)")
plt.xlabel("K-Value")
plt.ylabel("Compression Rate(%)")
plt.plot(x, y, color ="red")
plt.show()