# Patrick Kunst
# CSC 241
# Lab 2 Part 4


# A
def say_hello():
    print('Hello there!')

say_hello()

# B
def param_test(my_string):
    print('Parameter: ' + my_string)

param_test('Hello!')

# C
def return_square(my_num):
    square = my_num ** 2
    return square

my_square = return_square(5)
print('Square: ' + str(my_square))
