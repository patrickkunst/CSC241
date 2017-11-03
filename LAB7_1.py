# Patrick Kunst
# CSC 241
# Lab 7 Part 1

def sum_digits(num):
    num_sum = 0
    digit = 0

    while digit < len(str(num)):
        my_digit = str(num)[digit]
        num_sum += int(my_digit)
        digit += 1
    return num_sum

positive = False

while positive == False:
    number = eval(input('Please enter a positive whole number: '))
    if number >= 0:
        positive = True

my_sum = sum_digits(number)

print('The sum of the digits in the value {} is {}.'.format(number, my_sum))
