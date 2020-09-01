from datetime import datetime


def print_grid(grid):
    for x in range(9):
        if x == 3 or x == 6:
            print('- - - - - - - - - - - ')
        for y in range(9):
            if y == 3 or y == 6:
                print(' | ', end='')
            if y != 8:
                print(grid[x][y], end='')
                if not (y == 2 or y == 5):
                    print(' ', end='')
            else:
                print(grid[x][y])

    print("\n---------------------")
    print("---------------------")
    print("---------------------\n")


def input_row(row_num):
    output_row = []
    row_string = input('Please enter the ' + str(row_num + 1) + ' row (numbers seperated with whitespaces): ').split()
    for number in range(len(row_string)):
        output_row.append(int(row_string[number]))
    return output_row


def input_grid():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for row in range(len(grid)):
        grid[row] = input_row(row)
    return grid


def check_row(grid, row_num, column_num, value):
    for number in range(8):
        if number == column_num:
            continue
        if grid[row_num][number] == value:
            return False
    return True


def check_column(grid, row_num, column_num, value):
    for number in range(8):
        if number == row_num:
            continue
        if grid[number][column_num] == value:
            return False
    return True


def check_square(grid, row_num, column_num, value):
    if 0 <= row_num <= 2:
        row_range = [0, 1, 2]
    elif 3 <= row_num <= 5:
        row_range = [3, 4, 5]
    elif 6 <= row_num <= 8:
        row_range = [6, 7, 8]

    if 0 <= column_num <= 2:
        column_range = [0, 1, 2]
    elif 3 <= column_num <= 5:
        column_range = [3, 4, 5]
    elif 6 <= column_num <= 8:
        column_range = [6, 7, 8]

    for x in row_range:
        for y in column_range:
            if grid[x][y] == value:
                return False
    return True


def is_possible(grid, row_num, column_num, value):
    return (check_row(grid, row_num, column_num, value)
            and check_column(grid, row_num, column_num, value)
            and check_square(grid, row_num, column_num, value))


def find_next_empty(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return x, y
    return None


# test_grid = [[0, 4, 0, 0, 1, 0, 8, 0, 0],
#              [0, 0, 0, 4, 0, 0, 0, 0, 0],
#              [0, 3, 6, 0, 7, 0, 0, 0, 0],
#              [1, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 6, 0, 9, 4, 0, 5],
#              [0, 0, 0, 8, 2, 0, 0, 6, 0],
#              [0, 7, 8, 0, 0, 0, 5, 0, 0],
#              [0, 0, 0, 0, 4, 0, 0, 3, 0],
#              [3, 0, 0, 0, 0, 5, 9, 0, 0]]


def solve(grid,steps=False):
    current = find_next_empty(grid)
    if steps:
        print_grid(grid)
    if current == None:
        if not steps:
            print_grid(grid)
        return True
    else:
        row, column = current
    for value in range(1, 10):
        if is_possible(grid, row, column, value):
            grid[row][column] = value

            if solve(grid,steps):
                return True

            grid[row][column] = 0
    return False


print("Welcome to Sudoku puzzle solver!")
grid = input_grid()
start = datetime.now()
start_time = start.strftime("%H:%M:%S")
print("Your puzzle looks like this:\n")
print_grid(grid)
x = input("Do you want to see steps of the solution (y/n)? ")
if x=="y" or x=="Y":
    solve(grid,True)
else:
    print("This is your solution:")
    solve(grid)
print("Starting Time :", start_time)
end = datetime.now()
end_time = end.strftime("%H:%M:%S")
print("Ending Time :", end_time)
duration = end - start
print("Duration :", duration)
