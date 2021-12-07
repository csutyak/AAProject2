import sys
import re
import os
import numpy as np
import matplotlib.pyplot as plt
#2 args
#|size of original image.ascii - size of aproximated image|
#---
#size of orignal image.ascii

#3 args
#|size of orignal image.binary - size of approximated image|
#---
#size of ofrignal image binary

#size of original image.ascii
filename = sys.argv[1]

orginalAsciiSize = os.path.getsize(filename)

if len(sys.argv) == 3:
    filename = sys.argv[2]
#size of approximated image
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

#calculate the size of approximated image using every kValue

width = int(width)
height = int(height)

y =  np.zeros([255])

aproxImageSize = 0
for kValue in range(255):
    #base 6 bytes
    aproxImageSize = 6
    #U matrix; matrix size * 4 btyes
    aproxImageSize += (height * kValue) * 4
    #S matrix; kValue * 4 bytes
    aproxImageSize += (kValue) * 4
    #VT matrix; matrix size * 4 btyes
    aproxImageSize += (width * kValue) * 4

    workingNumerator = orginalAsciiSize - aproxImageSize
    if workingNumerator < 0:
        workingNumerator = workingNumerator * -1
    
    finalValue = workingNumerator / orginalAsciiSize
    y[kValue] = finalValue
 
# data to be plotted
x = np.arange(0, 255)

# plotting
plt.title("Compression Rate bytes (twoBalls_b.pgm)")
plt.xlabel("K-Value")
plt.ylabel("Compression Rate(%)")
plt.plot(x, y, color ="red")
plt.show()
