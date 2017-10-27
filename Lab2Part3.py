# Patrick Kunst
# CSC 241
# Lab 2 Part 3

# A
name = input('Enter your name: ')
for x in name:
    print(x)

# B

print(name[::-1])

# C
name_index = 0
for y in name:
    print(str(name_index) + ': ' + y)
    name_index += 1
