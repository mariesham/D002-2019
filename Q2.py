
# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
            if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
                return True
            return False
def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
    return False
def check_diagonal(cells):
    for i in range(0, 3):
        if cells[2][0] == cells[1][1] == cells[0][2] != ' ' or cells [0][0]== cells[1][1]==cells[2][2] !=' ':
            return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
xo=0
printcell(cells)
while ((check(cells)) == False):
    if xo%2==0:
        print("Player 1's turn.")
        col = int(input("Please enter column\n"))
        row = int(input("Please enter row\n"))
        if cells[row][col] == ' ':
            cells[row][col]='X'
            xo=xo+1
        else:
            print("It is already taken")
    else:
        print("Player 2's turn.")
        col=  int(input("Please enter column\n"))
        row = int(input("Please enter row\n"))
        if cells[row][col] == ' ':
            cells[row][col]='0'
            xo=xo+1
        else:
            print("It is already taken")
   
    printcell(cells)


    if (check(cells))== True:
        print("Game Over")
        if xo%2==0:
            print("Player 1 wins!")
        elif xo==9:
            print("It's a tie. Restart the game.")
            printcell(cells)
        else:
            print("Player 2 wins!")
            break
     
