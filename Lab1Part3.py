# Patrick Kunst
# CSC 241
# Lab 1 Part 3

# Program will have user enter the total and tip percentage, then will output the new total

check = eval(input('Check Total: '))
tip_percent = eval(input('Tip Percent: '))

new_total = round(((1+(tip_percent/100)) * check), 2) #I looked up the rounding function to make it look like an actual dollar amount
print('Please pay: $' + str(new_total))
