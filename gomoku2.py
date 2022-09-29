"""Name: Saiful Islam Shovo,ID:1608714
This is a game called gomoku where user can input rows and columns for making a board this is a game played with two players:
 computer and human. In human turn it will take input of rows and columns and it will put stone 'O' inside the board.
 In machine turn it will randomly choose a spot in the board and if it is taken, then it will find another one.
  print_board -->this takes rows and column and make a board that contains rows and columns
  humanturn() -->this function takes human two numbers as rows and columns and put 'O' on that place in the board
  Random_Machine_Turn() -->this function puts 'X' on random places in the board
  Smart_Machine()-->this function puts 'X' where there is the best possibility for human to put stone
  Check_Connected_num(row, column ,stone) -->this function counts the longest connected stones and return the number of that connected stones
  Machine_Turn(option) -->this function takes 1 or 2 as a input and runs random machine function if the input is 1 and runs smart machine if the input is 2
  All_spot_taken -->this function checks if all the spots are taken or not
  """

import random  # this is for the machine turn function
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
y = input('Input the number of rows that you want:(1-10) ')
while y not in number or not y.isdigit:  # if string y is not in number list and y is not digit then it prints wrong input
    print('Wrong Input')
    y = input('Input the number of rows that you want:(1-10) ')
z = input('Input the number of columns that you want:(1-10) ')
while z not in number or not z.isdigit:
        print('Wrong Input')
        z = input('Input the number of columns that you want:(1-10): ')

m = int(y)
n = int(z)



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
 

board = [[' ']*n for i in range(m)] #it convert the board into 2D board

def humanturn():
    """this function takes human two numbers as rows and columns and put 'O' on that place in the board"""
    print('=' * 15) #it prints '=' 15 times
    print('Human"s Turn')
    print('=' * 15)
    z=[]
    u = []

    for i in range(1, m+1): #it goes through the number of rows
        z.append(str(i)) #it adds i as a string in the empty list z
    k = input('Input The ROW where you want to put your stone between 1 and ' + str(m)+': ')
    while k not in z: #this while loop checks the input of rows
        print('Wrong Input')
        k = input('Input The ROW where you want to put your stone between 1 and ' + str(m) + ': ')

    for j in range(1, n+1): #it goes through the number of columns
        u.append(str(j)) #it adds j as a string in the empty list u
    l = input('Input The COLUMN where you want to put your stone between 1 and ' + str(n) + ' : ')
    while l not in u: #this while loop checks the input of columns
        print('Wrong Input')
        l = input('Input The COLUMN where you want to put your stone between 1 and ' + str(n) + ' : ')


    x = int(k)
    y = int(l)

    print('=' * 15)
    print('Human"s Choice is '+ str(x) + ',' + str(y))
    print('=' * 15)
    while board[x - 1][y - 1] != ' ': #when the spot in the board is not empty
        print('The spot ' + '(' + k+ ',' +l  + ')' + ' has been already taken!!')
        print('Enter the values again')
        k = input('Input The ROW where you want to put your stone between 1 and ' + str(m)+': ')
        while k not in z:
            print('Wrong Input')
            k = input('Input The ROW where you want to put your stone between 1 and ' + str(m)+': ')
        l = input('Input The COLUMN where you want to put your stone between 1 and ' + str(n) + ' : ')
        while l not in u:
            print('Wrong Input')
            l = input('Input The COLUMN where you want to put your stone between 1 and ' + str(n) + ' : ')
        x = int(k)
        y = int(l)
        print('=' * 15)
        print('Human"s Choice is '+ str(x) + ',' + str(y))
        print('=' * 15)
    global human_row, human_column #it makes this two variables global
    human_row = x
    human_column = y
        


    board[x - 1][y - 1] = 'O' #it puts 'O' in the row x and column y

def Random_Machine_Turn():
    """this function puts 'X' on random places in the board"""
    print('=' * 15)
    print('Random Machine"s Turn')
    print('=' * 15)

    for x in range(1):
        r  = random.randint(1, m) #it choose a random value from 1 to n

    for Y in range(1):
        c = random.randint(1, n) #it choose a random value from 1 to m


    while board[r - 1][c - 1] != ' ': #when the spot in the board is not empty
        print('The spot ' + '(' + str(r)+ ',' +str(c)  + ')' + ' has been already taken!!')
        v = (input("Press 'c' key if you want machine to choose a random spot again!!: "))
        while v != 'c': #if other input is entered without 'c' then it will print wrong input
          print('Wrong Input')
          v = (input('Press \'c\' to continue for machine\'s turn: '))
        if v == 'c':
            for x in range(1):
                r = random.randint(1, m)  # it choose a random value from 1 to n

            for Y in range(1):
                c = random.randint(1, n)  # it choose a random value from 1 to m

    print('=' * 15)
    print('Random Machine"s Choice is ' + str(r) + ',' + str(c))
    print('=' * 15)
    board[r - 1][c - 1] = 'X' #it puts 'X' in the row r and column c
    global machine_row, machine_column #it makes the variables global
    machine_row = r
    machine_column = c



def Smart_Machine():
    """this function puts 'X' where there is the best possibility for human to put stone"""
    print('===============')
    print('Smart Machine"s Turn')
    print('===============')
    max_value = 0

    for i in range(m): #it goes through 0 to row numbers of the board
        i += 1 #it will add position 10 and remove 0
        for j in range(n): #it goes through 0 to column numbers of the board
            j += 1 #it will add position 10 and remove 0
            if board[i-1][j-1] != ' ': #if the board position is empty it will continue
                continue
            else:
                board[i-1][j-1] = 'O' #if the board position has human stone then it will put stone near the more connected human stone
                if max(Row_check(i, j, 'O'), Column_check(i, j, 'O'), Right_Diagonal_check(i, j, 'O'), Left_Diagonal_check(i, j, 'O')) > max_value: #it will find the long connected stone position
                    max_value = max(Row_check(i, j, 'O'), Column_check(i, j, 'O'), Right_Diagonal_check(i, j, 'O'),Left_Diagonal_check(i, j, 'O'))
                    best_position_row = i
                    best_position_column = j
                    board[i-1][j-1] = ' ' #if the space near the long connected stone is empty
                else:
                    board[i-1][j-1] = ' '
    global machine_row, machine_column
    machine_row = best_position_row
    machine_column = best_position_column
    print('Smart Machine"s Choice is {},{}'.format(best_position_row,best_position_column))
    print('===============')
    board[best_position_row-1][best_position_column-1] = 'X'



def Check_Connected_num(row, column ,stone):
     """this function counts the longest connected stones and return the number of that connected stones"""
     Check_Connected_num = max(Column_check(row, column, stone), Row_check(row, column, stone), Left_Diagonal_check(row, column, stone), Right_Diagonal_check(row, column, stone))
     winner = max(Column_check(row, column, stone), Row_check(row, column, stone), Left_Diagonal_check(row, column, stone), Right_Diagonal_check(row, column, stone))
     return winner

def Row_check(row, column,stone):
    """this function checks the row if it has connected stone in rows and return the number"""
    total = 0
    for i in range(column, n + 1): #it goes through input column to board column number + 1
            if board[row - 1][i - 1] == stone:
                total += 1
            else:
                break
    for j in range(column - 1, 0, -1): #it goes through input column -1 to 0 in reverse way
            if board[row - 1][j - 1] == stone:
                 total += 1
            else:
                 break
    return total
def Column_check(row, column, stone):
    """this function checks the column if it has connected stone in columns and return the number"""
    total = 0
    for i in range(row, m + 1): #it goes through input row to board row + 1
        if board[i - 1][column - 1] == stone:
            total += 1
        else:
            break
    for j in range(row - 1,0, -1): #it goes through input row -1 to 0 in reverse way
            if board[j - 1][column - 1] == stone:
                total += 1
            else:
                break
    return total
def Left_Diagonal_check(row, column, stone):
    """this function checks the left diagonal if it has connected stones and return the number"""
    total = -1 #it is for ignoring the chances of counting the input row and column twice
    (x, y) = (row, column) #it creates 2 new variables for inout row and column as those variables are going to change
    while 0 < x <= m and 0 < y <= n and board[x - 1][y - 1] == stone: #this while loop is checking the input row and column are not out of range
        total += 1
        x -= 1 #decreasing the row by one each time when above condition is true
        y += 1 #increasing the column by one each time when above condition is true
    (x, y) = (row, column)
    while 0 < x < m and 0 < y <= n and board[x-1][y-1] == stone:
        total += 1
        x += 1
        y -= 1
    return total


def Right_Diagonal_check(row,column,stone):
    """this function checks the right diagonal if it has connected stones and return the number"""
    total =- 1
    (x, y) = (row, column)
    while 0 < x <= m and 0 < y <= n and board[x - 1][y - 1] == stone:
        total += 1
        x -= 1 #decreasing both the input row and column
        y -= 1
    (x, y) = (row, column)
    while 0 < x <= m and 0 < y <= n and board[x - 1][y - 1] == stone:
        total += 1
        x += 1 #increasing both the input row and column
        y += 1
    return total

   
    


def Machine_Turn(option):
        """this function takes 1 or 2 as a input and runs random machine function if the input is 1 and runs smart machine if the input is 2"""
        if (option == '1'): #if option is '1' then it will take c as input and return 'Random Machine'
            c = input('Press \'c\' to continue for machine\'s turn: ')
            while c != 'c':
                print('wrong input')
                c = input('Press \'c\' to continue for machine\'s turn again: ')
            if c == 'c':
                return Random_Machine_Turn()

        elif (option == '2'): #if option is '2' then it will take c as input and return 'Smart Machine'
            c = input('Press \'c\' to continue for machine\'s turn again: ')
            while c != 'c':
                print('wrong input')
                c = input('Press \'c\' to continue for machine\'s turn again: ')
            if c == 'c':
                return Smart_Machine()


def all_spots_taken():
    """this function checks if all the spots are taken or not"""
    for i in board: #it goes through the each line in the board
        for j in i: #it goes through the each spot in the line
            if j == ' ': #if all those spots are empty
                return False #then it will return False


    return True

print_board()
option = input('Who do you want to play with? 1.Random machine 2.Smart machine: ') #asks for entering '1' or '2' for machine turn
while option not in ('1', '2'): #if user put anything else with '1' or '2' then it says 'wrong input' and asks for input again
    print('wrong input')
    option = input('Who do you want to play with? 1.Random machine 2.Smart machine: ')
while True: #this is a infinite loop
    humanturn()
    stone='O' #it takes stone value 'O' for the 'Connect_Connected_num'
    if Check_Connected_num(human_row,human_column,stone)  >= 5: #if 'Connect_Connected_num' returns number greater than and equals to 5
            print_board()
            print("*************************")
            print("CONGRATULATIONS!!! Human Win!!!")
            print("*************************")
            break

    elif all_spots_taken(): #if all_spots_taken returns true then
            print_board()
            print('*' * 25)
            print('No more spot left. Game Ended.')
            print('*' * 25)
            break
    print_board()
    Machine_Turn(option)
    stone = 'X' #it takes stone value 'X' for the 'Connect_Connected_num'
    if Check_Connected_num(machine_row, machine_column, stone) >= 5: #if 'Connect_Connected_num' returns number greater than and equals to 5
            print_board()
            print("*************************")
            print("CONGRATULATIONS!!!! Machine Win!!!")
            print("*************************")
            break
    if all_spots_taken(): #if 'all_spot_taken' is true than it prints 'No more spot left. Game Ended.'
                print_board()
                print('*' * 25)
                print('No more spot left. Game Ended.')
                print('*' * 25)
                break
    print_board()



    

