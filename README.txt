How to run our AAProject2: SVD & PCA
    There are five ways to run our project:

    1. Command to convert .pgm file from ascii to bytes:
        ./main.py 1 <imageName>.pgm
        * <imageName>.pgm is a .pgm file of type 2 that must be in the same folder
        * This will return <imageName>_b.pgm

    2. Command to reverse the previous command; making a .pgm file from bytes back to ascii
        ./main.py 2 <imageName>_b.pgm
        * <imageName>_b.pgm is the name of the file outputted in the previous command. 
        * This will return <imageName>_copy.pgm

    3. Command to run SVD on an .pgm file
        ./main.py 3 <imageName>.pgm k
        * <imageName>.pgm is a .pgm file of type 2 that you want to be compressed
        * 'k' is the rank of the .pgm image that you would like to return
        * This will return <imageName>_b.pgm.SVD

    4. Command to reverse the SVD:
        ./main.py 4 <imageName>_b.pgm.SVD
        * <imageName>_b.pgm>SVD is the output file name from command 3
        * This will return <imageName>_k.pgm

    5. Command to run PCA portion
        ./main.py 5
        * There is already a dataset, BankChurners.csv, that is being run from
        * There is nothing to return although there is some output. Alot of the output is commented out because
          it will not run on terminal. However, if you were to comment out the output and run it on a IDE like 
          Jupyter Notebooks, there will be ouputs of graphs and matrices. 

    *Note: There are some libraries that are needed to run any part of the application. Make sure the following are
    already downloaded into your Python environment:
        * sys
        * numpy
        * re
        * matplotlib
        * scipy
        * pandas
        * seaborn
        * sklearn
