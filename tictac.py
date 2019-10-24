#a program to play tic tac toe.

print("\n\tTic Tac Toe\n\n\tBy Luke Ireland\n")
n = int(input("Enter the size of the playing board\n"))
player1_name = input("Enter player 1 name:\n")
player2_name = input("Enter player 2 name:\n")

game_matrix = [[0] * n for i in range(n)]
grid_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def row(n):
    #prints a new row (this never needs the game matrix)
    i3 = 0
    while(i3<n):
        print(" ---", end = " ")
        i3 = i3 + 1
    print("\n")

def column(n, game_matrix, i5):
    #prints a new sequence of columns, depending on what the game matrix says
    i4 = 0
    while(i4<=n):
        if(i4<n and i4 != 0):
            #not the first one or last one
            if(game_matrix[i5][i4] == 0):
                print(" |  ", end = " ")
            if(game_matrix[i5][i4] == 1):
                print(" | X", end = " ")
            if(game_matrix[i5][i4] == 2):
                print(" | O", end = " ")
        if(i4 == 0):
            #the first one
            if(game_matrix[i5][i4] == 0):
                print("|  ", end = " ")
            if(game_matrix[i5][i4] == 1):
                print("| X", end = " ")
            if(game_matrix[i5][i4] == 2):
                print("| O", end = " ")
        if(i4 == n):
            #the last one
            print(" |  {}".format(i5+1))
        i4 = i4 + 1
    print("\n")

def play_game(n, game_matrix):
    print("\n")
    i3 = 0
    while(i3<n):
        print("  {} ".format(grid_letters[i3]), end = " ")
        i3 = i3 + 1
    print("\n")

    i5 = 0
    while(i5<n):
        row(n)
        column(n, game_matrix, i5)
        i5 = i5 + 1
    row(n)

def win(game_matrix):
    #there are a few ways a player can win. they can get a full row, or they
    #can score a full column, or they can score a full diagonal.
    #This function should return 0 if no one has won *yet*, 1 if player 1 has
    #won, 2 is player 2 has won,and 3 if no one has won and the game is over.

    #we begin by scanning all rows - checking if player 1 has won
    i6 = 0
    i7 = 0
    while(i6<n):
        i7 = 0
        while(i7<n):
            if(game_matrix[i6][i7] != 1):
                break
            if(i7 == n-1):
                return 1
            i7 = i7 + 1
        i6 = i6 + 1

    #now we scan all rows, checking if player 2 has won
    i8 = 0
    i9 = 0
    while(i8<n):
        i9 = 0
        while(i9<n):
            if(game_matrix[i8][i9] != 2):
                break
            if(i9 == n-1):
                return 2
            i9 = i9 + 1
        i8 = i8 + 1

    # now we scan all columns - checking if player 1 has won
    i10 = 0
    i11 = 0
    while(i10<n):
        i11 = 0
        while(i11<n):
            if(game_matrix[i11][i10] != 1):
                break
            if(i11 == n-1):
                return 1
            i11 = i11 + 1
        i10 = i10 + 1

    # now we scan all columns - checking if player 2 has won
    i12 = 0
    i13 = 0
    while(i12<n):
        i13 = 0
        while(i13<n):
            if(game_matrix[i13][i12] != 2):
                break
            if(i13 == n-1):
                return 2
            i13 = i13 + 1
        i12 = i12 + 1

    #finally, we need to check to see if some has won via diagonals
    #scan diagonal (left to right) checking to see if player 1 has won
    i14 = 0
    while(i14<n):
        if(game_matrix[i14][i14] != 1):
            break
        if(i14 == n-1):
            return 1
        i14 = i14 + 1

    #scan the other diagonal (right to left) checking to see if player 1 has won
    i15 = 0
    i16 = n-1
    while(i15<n):
        if(game_matrix[i15][i16] != 1):
            break
        if(i15 == n-1):
            return 1
        i15 = i15 + 1
        i16 = i16 - 1

    #again scan left to right diagonal, checking to see if player 2 has won
    i17 = 0
    while(i17<n):
        if(game_matrix[i17][i17] != 2):
            break
        if(i17 == n-1):
            return 2
        i17 = i17 + 1

    #finally, scan right to left diagonal, checking to see if player 2 has won
    i18 = 0
    i19 = n-1
    while(i18<n):
        if(game_matrix[i18][i19] != 2):
            break
        if(i18 == n-1):
            return 2
        i18 = i18 + 1
        i19 = i19 - 1

    # if reaching this point, there are no winners this round
    # now we must check if the game is over with no winners
    i20 = 0
    i21 = 0
    while(i20<n):
        i21 = 0
        while(i21<n):
            if(game_matrix[i20][i21] == 0):
                return 0
            i21 = i21 + 1
        i20 = i20 + 1
    #if reaching this point, there are no winners and game is over
    return 3

def swap(matrix):
    # a function to swap the components of a matrix around
    t = matrix[0]
    matrix[0] = matrix[1]
    matrix[1] = t

# main function starts here

#start the game
play_game(n, game_matrix)

while(win(game_matrix) == 0):

    while(1):
        a = input("{}'s turn\n".format(player1_name))
        player1 = [i22 for i22 in str(a)]
        #correct the order
        if(player1[1].isdigit()):
            swap(player1)

        player1[0] = int(player1[0])

        #turn letter into integer
        i30 = 0
        while(i30<n):
            if(player1[1] == grid_letters[i30]):
                break
            i30 = i30 + 1
        player1[1] = i30

        a1 = player1[0] - 1
        a2 = player1[1]

        if(game_matrix[a1][a2]==0):
            game_matrix[a1][a2] = 1
            break
        else:
            print("that spot has already been picked, try again...\n")

    if(win(game_matrix)!=0):
        break

    play_game(n, game_matrix)

    while(1):
        b = input("{}'s turn\n".format(player2_name))
        player2 = [i23 for i23 in str(b)]
        #correct the order
        if(player2[1].isdigit()):
            swap(player2)

        player2[0] = int(player2[0])

        #turn letter into integer
        i31 = 0
        while(i31<n):
            if(player2[1] == grid_letters[i31]):
                break
            i31 = i31 + 1
        player2[1] = i31

        b1 = player2[0] - 1
        b2 = player2[1]

        if(game_matrix[b1][b2]==0):
            game_matrix[b1][b2] = 2
            break
        else:
            print("that spot has already been picked, try again...\n")

    play_game(n, game_matrix)

#game over, now print the result
if(win(game_matrix)==1):
    print("\n\n", "**", player1_name, " wins!! **\n")
if(win(game_matrix)==2):
    print("\n\n", "**", player2_name, " wins!! **\n")
if(win(game_matrix)==3):
    print("\n\tNo one wins this game :(\n\n")
play_game(n, game_matrix)
