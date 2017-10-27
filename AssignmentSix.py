# Patrick Kunst
# CSC 241
# Assignment 6

def check_sudoku(file):
    sudoku = file.read()
    file.close()
    sudoku = sudoku.split('\n')

    x = 0
    for row in sudoku: # Convert to 2D list
        row = row.split(' ')
        sudoku[x] = row
        x += 1

        index = 0
        for y in row:# Convert to integers
            y = eval(y)
            row[index] = y
            index += 1

    row_err = []
    index = 0
    for row in sudoku:
        if sum(row) != 45:
            row_err.append(index)
        index += 1

    row_nums = []
    for row in row_err:# Gets the duplicate number
        for num in sudoku[row]:
            if sudoku[row].count(num) > 1:
                row_nums.append(num)
                break
    

    col_err = []
    col = 0
    while col < 9:# Check columns for errors
        sum_col = 0
        for x in range(9):
            sum_col += sudoku[x][col]
        if sum_col != 45:
            col_err.append(col)
        
        col += 1

    col_list = []
    for col in col_err:
        col_list.append([])

    row = 0
    index = 0
    for col in col_err:# To make it easier to find the duplicate number
        for row in range(9):
            col_list[index].append(sudoku[row][col])
        index += 1

    col_nums = []
    x = 0
    for col in col_list:
        for num in col_list[x]:
            if col.count(num) > 1:
                col_nums.append(num)
                break
            
            
    if len(row_err) == 0 and len(col_err) == 0:
        print('Sudoku verified!')

    if len(row_err) != 0:
        x = 0
        for row in row_err:
            row_string = ''
            for col in range(9):
                row_string += str(sudoku[row][col]) + ' '
            output = 'Row {} of 9:      {}   Bad Digit: {}'
            print(output.format(row_err[x] + 1, row_string, row_nums[x]))
            x += 1

    if len(col_err) != 0:
        x = 0
        for col in col_list:
            col_string = ''
            for num in range(9):
                col_string += str(col_list[x][num]) + ' '
            output = 'Column {} of 9:   {}   Bad Digit: {}'
            print(output.format(col_err[x] + 1, col_string, col_nums[x]))
            x += 1
    

name = input('Enter file name: ')
inFile = open(name)
check_sudoku(inFile)

