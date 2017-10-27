def change(amt):
    avail = [20, 10, 5, 1, .25, .10, .05, .01]
    sol = []

    while amt > 0:
        for x in avail:
            if x < amt:
                break
        sol.append(x)
        amt -= x
    return sol

print(change(28.43))
