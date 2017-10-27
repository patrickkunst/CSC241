# Patrick Kunst
# CSC 241
# Lab 5 Part 1

import random

def pizza_maker(num_tops):
    sizes = ['small', 'medium', 'large']
    crusts = ['extra thin crust', 'thin crust', 'deep dish', 'cheese crust']
    toppings = ['sausage', 'green pepper', 'onions', 'pepperoni', 'mushrooms', 'olives']

    if num_tops > len(toppings):
        return None
    user_size = random.choice(sizes)
    user_crust = random.choice(crusts)
    user_toppings = random.sample(toppings, num_tops)

    toppings_string = ''
    for x in user_toppings:
        if x == user_toppings[-1]:
            toppings_string += x
        elif x == user_toppings[-2]:
            toppings_string += x + ' and '
        else:
            toppings_string += x + ', '

    if user_size == 'small':
        price = 12.99
    elif user_size == 'medium':
        price = 14.99
    elif user_size == 'large':
        price = 16.99

    for x in user_toppings:
        price += 1

    price = round(price, 2)

    return [user_size, user_crust, toppings_string, price]

# Main Code

num = eval(input('Enter the numger of toppings you would like: '))
data = pizza_maker(num)

if data == None:
    print('Invalid number of toppings')
elif data[2] == '':
    print('You get a', str(data[0]), str(data[1]), 'pizza with no toppings costing $' + str(data[3]) + '.') #If toppings = 0
else:
    print('You get a', str(data[0]), str(data[1]), 'pizza with', str(data[2]), 'costing $' + str(data[3]) + '.')
