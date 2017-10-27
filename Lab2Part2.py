# Patrick Kunst
# CSC 241
# Lab 2 Part 2

# A
character = input("Enter a character: ")
if character == ' ':
    print('Space')

# B
number = eval(input('Enter a number: '))
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# C
num_one = eval(input('Enter a number: '))
num_two = eval(input('Enter another number: '))

if (num_one * num_two) < 0:
    print('Negative')
else:
    print('Positive')
