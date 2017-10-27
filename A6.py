# Patrick Kunst
# CSC 241
# Assignment 6

def check_sudoku(file_name):
    grid = file_name.read()
    grid = grid.split('\n') # I was going to do readlines but \n was in each element

    y = 0
    for x in grid:# Convert to 2D List
        x = x.split(' ')
        grid[y] = x
        y += 1

        index = 0
        for z in x:# Convert elements to integers
            z = eval(z)
            x[index] = z
            index += 1

    row_err = []
    col_err = []

    index = 0
    for x in grid:
        print(sum(x))# Debug
        if sum(x) != 45:
            row_err.append(index)
        index += 1
    print(row_err)#Debug

    rows = len(grid)
    cols = len(grid[0])
    col_num = 0
    for i in range(rows):
        col_sum = 0
        for j in range(cols):
            col_sum += grid[j][i]
        print(col_sum)
        
        if col_sum != 45:
            col_err.append(col_num)
        col_num += 1
        
    row_nums = []
    for x in row_err:# Gets the error number
        for i in grid[x]:
            index = 0
            count = 0
            while index <= 8:
                if i == grid[x][index]:
                    count += 1
                    if count > 1 and len(row_nums) == 0:
                        row_nums.append(i)
                    elif count > 1 and i != row_nums[-1]: #Prevents double counting
                        row_nums.append(i)
                        #Same outcome, but row_nums[-1] cannot be checked if there are no elements
                index += 1
    cols = []
    for x in col_err:
        cols.append([])
    
    
                    

    print(row_err) # Debug
    print(col_err) # Debug
    print(row_nums) # Debug
    print(cols)

    
    
file = open(input('Enter sudoku text file: '))
