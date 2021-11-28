import sys
from program1 import program1
from program2 import program2
from program3 import program3
from program4 import program4

#get arguments from user input
if sys.argv[1] == "1":
    program1(sys.argv[2])

if sys.argv[1] == "2":
    program2(sys.argv[2])

if sys.argv[1] == "3":
    program3(sys.argv[2], sys.argv[3])

if sys.argv[1] == "4":
    program4(sys.argv[2])