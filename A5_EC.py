# Patrick Kunst
# CSC 241
# Assignment 5 EC

import random

def calc_line(num_msgs, num_lines, rem_mode):
    net_lines = []
    for x in range(num_lines):
        net_lines.append(0)

    div = num_msgs // num_lines

    y = 0
    for x in net_lines:
        net_lines[y] = div
        y += 1

    rem = num_msgs % num_lines

    if rem_mode == 'round-robin':
        y = 0
        for x in range(rem):
            net_lines[y] += 1
            y += 1
    elif rem_mode == 'random':
        for x in range(rem):
            index = random.randint(0, len(net_lines) - 1)
            net_lines[index] += 1

    return net_lines

messages = eval(input('Enter number of messages: '))
lines = eval(input('Enter number of internet lines: '))
mode = input('round-robin or random?: ')
mode = mode.lower()

count = calc_line(messages, lines, mode)

print(count)
