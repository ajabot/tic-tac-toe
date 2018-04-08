#!/usr/bin/python
import sys

print "Tic Tac Toe"

#Displays the grid
def display_grid(grid):
    print "   A  B  C"
    for x in range(0, 3):
        sys.stdout.write(str(x+1))
        sys.stdout.write("  " + grid[x][0])
        sys.stdout.write("  " + grid[x][1])
        sys.stdout.write("  " + grid[x][2] + '\n')
    sys.stdout.flush()

#gets and checks the player's input
def player_input(player, grid):
    input_ok = False

    while not input_ok:
        player_column = ""
        player_row = ""

        while player_column != "a" and player_column != "b" and player_column != "c":
            player_column = raw_input(player + " player please enter column[A,B,C]: ")
            player_column = player_column.lower()
        
        while player_row != "1" and player_row != "2" and player_row != "3":
            player_row = raw_input(player + " player please enter row[1,2,3]: ")

        column = column_mapping[player_column]
        row = row_mapping[player_row]
        # the above loops avoid being out of range
        # so just checking if space is not taken
        if grid[row][column] == " ":
            grid[row][column] = player
            input_ok = True
        else:
            print("Space already taken")
            input_ok = False

    return grid

#checks if player cleared one of the columns
def won_column(player, grid):
    for x in range(0, 3):
        if grid[0][x] == player and grid[1][x] == player and grid[2][x] == player:
            return True

#checks if player cleared one of the rows
def won_row(player, grid):
    for x in range(0, 3):
        if grid[x][0] == player and grid[x][1] == player and grid[x][2] == player:
            return True

#checks if player cleared one of the diagonals        
def won_diagonals(player, grid):
    if (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player) or (grid[0][2] == player and grid[1][1] == player and grid[2][0] == player):
        return True

#checks if player has won the game
def has_player_won(player, grid):
    if won_column(player, grid):
        return True
    elif won_row(player, grid):
        return True
    elif won_diagonals(player, grid):
        return True

    return False
    
#init
grid = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

column_mapping = {"a": 0, "b": 1, "c": 2}
row_mapping = {"1": 0, "2": 1, "3": 2}

display_grid(grid)
over = False

nb_moves = 0

while not over:
    grid = player_input("X", grid)
    display_grid(grid)
    nb_moves += 1
    if has_player_won("X", grid):
        print("X won!")
        over = True
    #if we reached 9 moves and no one won, it's a draw
    elif nb_moves == 9:
        print("It's a draw")
        over = True
    else:
        grid = player_input("O", grid)
        display_grid(grid)
        if has_player_won("O", grid):
            print("O won!")
            over = True
        nb_moves += 1

print("Game Over")

