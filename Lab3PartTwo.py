# Patrick Kunst
# CSC 241
# Lab 3 Part 2

# Part A

fileA = open('Lab3_Output1.txt', 'w')

for x in range(1, 21):
    fileA.write(str(x) + ' ')

fileA.write('\n')
fileA.flush()
fileA.close()

# Part B

fileB = open('Lab3_Output1.txt', 'a')

fileB.write('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

fileB.flush()
fileB.close()

# Part C

fileC = open('Lab3_Output2.txt', 'w')

for x in range(1, 51):
    fileC.write(str(x))
fileC.write('\n')

fileC.flush()
fileC.close()

# Part D

fileD = open('Lab3_Output2.txt', 'w')
fileD.write(':-) \n')

fileD.flush()
fileD.close()
