import sys
from program1 import program1
from program2 import program2

#get arguments from user input
if sys.argv[1] == "1":
    program1(sys.argv[2])

if sys.argv[1] == "2":
    program2(sys.argv[2])

if sys.argv[1] == "3":
    print("running option 1!")