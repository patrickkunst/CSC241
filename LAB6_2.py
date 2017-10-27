# Patrick Kunst
# CSC 241
# Lab 6 Part 2

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(26):
    for j in range(10):
        for k in range(10):
            print(letters[i] + str(j) + str(k))
