#minesweeper
import random

#poulate the grid
def pop_field():
    minefield =[
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
        ]
    
    row_index = 0
    for row in minefield:
        mine = random.randint(0,4)
        minefield[row_index][mine] = "#"
        row_index += 1

    return minefield


#prints the game board for player to see
def game_state(game):
    row_index = 0
    print("\n    1    2    3    4    5")
    for row in game:
        row_index  += 1
        print(f"{row_index} {row}")
    


#check for mines
def check_mine(board, row, col):
    mine_counter = 0

    if col < 0 or col > 4:
        print("Invalid column number please try again.")
        return -1

    elif row < 0 or row > 4:
        print("Invalid row number please try again.")
        return -1

    else:
        if board[row][col] == "#":
            return -2
        else:
            mine_counter += check_NW(board, row, col)
            mine_counter += check_N(board, row, col)
            mine_counter += check_NE(board, row, col)
            mine_counter += check_W(board, row, col)
            mine_counter += check_E(board, row, col)
            mine_counter += check_SW(board, row, col)
            mine_counter += check_S(board, row, col)
            mine_counter += check_SE(board, row, col)
            return mine_counter

    
    
#checks the ajacent spaces for mines
def check_NW(board, row, col):
    if row - 1 >= 0 and col - 1 >= 0:
        if board[row - 1][col - 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0
    
def check_N(board, row, col):
    if row - 1 >= 0:
        if board[row - 1][col] == "#":
            return 1
        else:
            return 0
    else:
        return 0
    
def check_NE(board, row, col):
    if row - 1 >= 0 and col + 1 <= 4:
        if board[row - 1][col + 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0
    
def check_W(board, row, col):
    if col -1 >= 0:
        if board[row][col - 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0

def check_E(board, row, col):
    if col + 1 <= 4:
        if board[row][col + 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0

def check_SW(board, row, col):
    if row + 1 <= 4 and col - 1 >= 0:
        if board[row + 1][col - 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0 

def check_S(board, row, col):
    if row + 1 <= 4:
        if board[row + 1][col] == "#":
            return 1
        else:
            return 0
    else:
        return 0 

def check_SE(board, row, col):
    if row + 1 <= 4 and col + 1 <= 4:
        if board[row + 1][col + 1] == "#":
            return 1
        else:
            return 0
    else:
        return 0  

game =[
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
        ]

minefield = pop_field()
col = 0
row = 0

while True:
    game_state(game)
    #game_state(minefield)

    try:
        #take user input
        row = int(input("\nPlease enter a row number 1-5: "))
        col = int(input("Please enter a column number 1-5: "))
        #adjusts for the table
        row -= 1
        col -= 1

        result = check_mine(minefield, row, col)

        #updates game board or gives a game over
        if result == -2:
            print("That was a mine. Game over!")
            print(game_state(minefield))
            break
        else:
            game[row][col] = result
            minefield[row][col] = result


    #resets col and row if invalid option is selected
    except Exception:
        print("\nInvalid choice try again.")
        #print(Exception)
        #print(col, row)
        col = 0
        row = 0