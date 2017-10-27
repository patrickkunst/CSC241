# Patrick Kunst
# CSC 241
# Assignment 2

import math

# Part A

p1 = [1.4, 8.9]
p2 = [7.8, 12.6]

distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print('Distance: ' + str(distance))

# Part B

area = 10*(4+4+6+4+10+8) # area the paint needs to cover
cans = math.ceil(area/250)
print(str(cans) + ' cans')

# Part C

x = eval(input('Enter an x-coordinate: '))
y = eval(input('Enter a y-coordinate: '))

if ((x > p1[0]) and (x < p2[0])) and ((y > p1[1]) and (y < p2[1])):
    print(True)
else:
    print(False)

# Part D

list_d = [] # Empty list to append data to

for i in range(1, 151):
    if (i % 6 == 0):
        if (i % 4 != 0):
            list_d.append(i)
print(list_d)

# Part E

def average(s):
    'The average() function averages a list that is passed to it'
    avg = sum(s) / len(s)
    return avg

scores = [] # Empty list to store scores in
num_scores = eval(input('How many scores would you like to enter? '))
for s in range(1, num_scores + 1):
    scores.append(eval(input('Enter the score: ')))
avg_score = average(scores)

print('The average score is ' + str(avg_score) + '%')
