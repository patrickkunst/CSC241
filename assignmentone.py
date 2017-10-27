# Patrick Kunst
# CSC 241 Assignment 1


# Part A
farenheit = (9/5)*22 + 32
print('22 degrees Celcius is ' + str(farenheit) + ' degrees farenheit')

# Part B
print('popar' in 'Pseudohypoparathyroidism')

# Part C
list_c = ['Skip']
list_c.append('Broad')
list_c.append('Slippery')
list_c.append('Previous')
list_c.append('Transport')
list_c.append('Tab')

print(list_c)
print('The list has ' + str(len(list_c)) + ' items')
print('The longest string in the list is "' + str(max(list_c, key=len)) + '"')
print('The shortest string in the list is "' + str(min(list_c, key=len)) + '"')


# Part D
list_d = [70, 92, 68, 67, 89, 75, 89, 77, 81, 60, 81, 90]
print(list_d)
print(len(list_d))
print(min(list_d))
print(max(list_d))
print(sum(list_d)/len(list_d))

# Part E
list_e = ['Vito', 'Michael', 'Kay', 'Fredo', 'Connie', 'Luca']
print(min(list_e))
print(max(list_e))
