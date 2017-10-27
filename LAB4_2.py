# Patrick Kunst
# CSC 241
# Lab 4 Part 2

# A
my_list = ['qw', 'er', 'ty', 'ui', 'op', 'as']

# B
letters = 'qwertyuiopas'

# C
if 'ui' in my_list:
    print(my_list.index('ui'))

# D
if 'ui' in letters:
    print(letters.find('ui'))

# E
if 'r' in my_list:
    print(my_list.index('r'))

# F
if 'r' in letters:
    print(letters.find('r'))

# G
my_list.reverse()
print(my_list)

# H
reverse = ''
y = -1
for x in letters:
    reverse += letters[y]
    y -= 1

print(reverse)
