# Patrick Kunst
# CSC 241
# Assignment 3 Part B

hour = 11
minute = 32
second = 21

time_fmt = '{}:{}:{}'
print(time_fmt.format(hour, minute, second))

thrones = ['A Game of Thrones', 'George R.R. Martin', 2011, 864, 'Bantam Books']
got_fmt = '{} was written by {}, and was published by {} in {}. It has {} pages'
print(got_fmt.format(thrones[0], thrones[1], thrones[4], thrones[2], thrones[3]))

numbers = [1, 44, 333, 2, 11, 4, 33, 222, 444, 3, 111, 22]
numbers.sort()
num_fmt = '{:4}    {:04d}    {:<4}'
for x in numbers:
    print(num_fmt.format(x, x, x))

dec_nums = [27.4, 1.999999, 399.2, 100.00, 154.89]
dec_nums.sort()

dec_fmt = '''
Lowest:    ${:.2f}
Middle:  ${:.2f}
Highest: ${:.2f}'''

print(dec_fmt.format(dec_nums[0], dec_nums[2], dec_nums[-1]))

flo_nums = [72, 101, 108, 108, 111, 32, 115, 116, 117, 100, 101, 110, 116, 33]
char_fmt = '{:c}'
for x in flo_nums:
    print(char_fmt.format(x), end = '')
