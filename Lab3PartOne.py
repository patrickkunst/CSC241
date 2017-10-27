# Patrick Kunst
# CSC 241
# Lab 3 Part 1

def file():# To make pasting the right path in easier
    the_file = open('C:\\Users\\Patrick\\Downloads\\Lab3_Input.txt')
    return the_file

# Part A

fileA = file()
print(fileA.readline())

fileA.close()

# Part B

fileB = file()
linesB = fileB.readlines()
print('Number of lines:', len(linesB))

fileB.close()

# Part C

fileC = file()
fileC_text = fileC.read()
print('Number of characters:', len(fileC_text))

fileC.close()

# Part D

fileD = file()
fileD_lines = fileD.readlines()
print(fileD_lines[-1])

# Part E

fileE = file()
fileE_text = fileE.read()
print("Appearances of 'mask':", fileE_text.count('mask'))

fileE.close()
