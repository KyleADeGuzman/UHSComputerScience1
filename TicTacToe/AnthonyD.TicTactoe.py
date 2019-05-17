
# Python 3 
# I Change the python version to 3.0 instead of 2.7
print("------DONE BY ANTHONY AND JOHN------")
print("Welcome to Tic Tac Toe!")
print("PLayer 1 you are X. ")
print("Player 2 you are O. ")
print("Rules: Pick a spot on the board. To win, connect 3 in a row/column or diaonally.")
print("Here are the posotions on the board: ")
print("------------------------------------")
TicTacToe = ['o', '1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 1
def PrintGrid():
    print("     |     |     ");
    print("  " + TicTacToe[1] + "  |  " + TicTacToe[2] + "  |  " + TicTacToe[3] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TicTacToe[4] + "  |  " + TicTacToe[5]+"  |  " + TicTacToe[6] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TicTacToe[7] + "  |  " + TicTacToe[8]+"  |  " + TicTacToe[9] + "  ")
    print("     |     |     ");
    
    
def Check():
    if((TicTacToe[1] == TicTacToe[2]) and (TicTacToe[2] == TicTacToe[3])):
        return 1
    
    elif((TicTacToe[1] == TicTacToe[4]) and (TicTacToe[4] == TicTacToe[7])):
        return 1

    elif((TicTacToe[1] == TicTacToe[5]) and (TicTacToe[5] == TicTacToe[9])):
        return 1

    elif((TicTacToe[2] == TicTacToe[5]) and (TicTacToe[5] == TicTacToe[8])):
        return 1

    elif((TicTacToe[3] == TicTacToe[6]) and (TicTacToe[6] == TicTacToe[9])):
        return 1

    elif((TicTacToe[3] == TicTacToe[5]) and (TicTacToe[5] == TicTacToe[7])):
        return 1

    elif((TicTacToe[4] == TicTacToe[5]) and (TicTacToe[5] == TicTacToe[6])):
        return 1

    elif((TicTacToe[7] == TicTacToe[8]) and (TicTacToe[8] == TicTacToe[9])):
        return 1

    elif(TicTacToe[1] != '1' and TicTacToe[2] != '2' and TicTacToe[3] != '3' and TicTacToe[4] != '4' and TicTacToe[5] != '5'
    and TicTacToe[6] != '6' and TicTacToe[7] != '7' and TicTacToe[8] != '8' and TicTacToe[9] != '9'):
            return 0

    else:
        return -1
    



player = player % 2
i = -1
while i == -1:
    PrintGrid()
    if player % 2:
        player = 1
    else:
        player = 2
    while True:
        try:
            choice = int(input("Player " + str(player) + ", enter a number: "))
            choice = choice + 0
            print("You entered the number: "+ str(choice))
            break
        except:
            print ("Please enter a number, not text!")
    play = player
    if player == 1:
        play = 'X'
    else:
        play = 'O'

    if (choice == 1 and TicTacToe[1] == '1'):
        TicTacToe[1] = play

    elif(choice == 2 and TicTacToe[2] == '2'):
        TicTacToe[2] = play

    elif(choice == 3 and TicTacToe[3] == '3'):
        TicTacToe[3] = play

    elif(choice == 4 and TicTacToe[4] == '4'):
        TicTacToe[4] = play

    elif(choice == 5 and TicTacToe[5] == '5'):
        TicTacToe[5] = play

    elif(choice == 6 and TicTacToe[6] == '6'):
        TicTacToe[6] = play

    elif(choice == 7 and TicTacToe[7] == '7'):
        TicTacToe[7] = play

    elif(choice == 8 and TicTacToe[8] == '8'):
        TicTacToe[8] = play

    elif(choice == 9 and TicTacToe[9] == '9'):
        TicTacToe[9] = play
    else:
        print("illegal move!")
        player = player - 1
    
    player = player + 1
    i = Check()
PrintGrid()
if(i == 1):
    print("Player " + str(player-1) +" won!")
else:
    print("Woah! That's a tie!")
while True:
    print("YOU WON!" )
    break
