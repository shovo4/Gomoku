def Row_check(row, column, stone):
    total = 0
    for x in range(row, m):
        if board[x][column] == stone:
            total += 1
        else:
            break
    for y in range(row,0,-1):
            if board[y-1][column] == stone:
                total += 1
            else:
                break
    return total
def Column_check(row, column,stone):
    total = 0
    for x in range(column,n):
                if board[row][x] == stone:
                    total += 1
                else:
                    break
    for y in range(column, 0, -1):
                if board[row][y-1] == stone:
                    total += 1
                else:
                    break
    return total
def Right_Diagonal_check(row, column, stone):
    total = 0
    if row <= column:
        for x in range(column, n+1):
            if board[row - 1 + (x - column)][x - 1] == stone:
                total += 1
            else:
                break
        for y in range(row-1,0,-1):
            if board[y-1][column-1+(y-row)] == stone:
                total += 1
            else:
                break
    else:
        for x in range(row,m + 1):
            if board[x - 1][column - 1 + (x - row)] == stone:
                total += 1
            else:
                break
        for y in range(column-1,0,-1):
            if board[row - 1 + (y - column)][y - 1] == stone:
                total += 1
            else:
                break
    return total
def Left_Diagonal_check(row,column,stone):
    total = 0
    if row + column <= 11:
        for x in range(row, 0, -1):
            if board[x - 1][column - 1 - (x - row)] == stone:
                total += 1
            else:
                break
        for y in range(column-1, 0, -1):
            if board[row - 1 - (y - column)][y - 1] == stone:
                total += 1
            else:
                break
    else:
        for x in range(column, n + 1):
            if board[row - 1 - (x - column)][x - 1] == stone:
                total += 1
            else:
                break
        for y in range(row, m + 1):
            if board[y - 1][column - 1 - (y - row)] == stone:
                total += 1
            else:
                break
    return total

def print_board():
    """this takes rows and column and make a board that contains rows and columns"""
    print('    ', end='')  #this add spaces on the left side for column numbers
    for i in range (1, n + 1): #this for loop goes throuh the number from 1 to n
        print(i, end = ' ') # it prints the column numbers on the top
    print() #it adds a line after column numbers
    for i in range(1, m + 1): #this for loop goes through the number from 1 to m
        print('  ', end = ' ')
        
        for j in range (1, n + 1): #this for loop goes through the number from 1 to n
            print('+-', end='') #this prints '+-' line by line
        print('+') #this add one more '+' after each line

        if i < 10:
            print('  ', end = '') #if i is less than 10 than it adds two spaces
            print(i, end = '')
        if i == 10:
            print(' ', end = '') #if i is equal 10 than it adds one space
            print(i, end = '')
        for k in range (1, n + 1):
            print('|'+ str(board[i - 1][k - 1]), end ='') #it prints '|' line by line
        print('|') #it prints one more | after each line
    print('   ', end='') #it adds space on the left side before the last line
    for j in range (1, n + 1):
        print('+-', end ='') #it prints the last line
    print('+') #it prints one more '+' in the last line


m=10
n=10
board=[[' ']*n for i in range(m)]
board[2][4]='O'
board[3][3]='O'
board[4][2]='O'
board[5][1]='O'
board[1][5]='O'
board[2][6]='O'
board[0][8]='O'
print_board()
print(Left_Diagonal_check(6,2,'O'))
