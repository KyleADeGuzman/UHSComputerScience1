#Partner Names: Ibn Muhammad, Amanda Dawson-Annan, Lilli Antwi
#Create a dictionary representing the positions/values in a tic tac toe board

theBoard={'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
# print(theBoard)

#Create a function that prints a tic tac toe board to the screen

def printBoard(board):
    print(board['1'] + '  |' + board['2'] + '   |'+board['3'])
    print('---+----+---')
    print(board['4'] + '  |' + board['5'] + '   |'+board['6'])
    print('---+----+---')
    print(board['7'] + '  |' + board['8'] + '   |'+board['9'])
# printBoard(theBoard)

#Create a function that decides if a player has won

def winCheck(board):
    if (board['1']=='X' and board['2']=='X' and board['3']=='X') or (board['4']=='X' and board['5']=='X' and board['6']=='X') or (board['7']=='X' and board['8']=='X' and board['9']=='X') or (board['1']=='X' and board['4']=='X' and board['7']=='X') or (board['2']=='X' and board['5']=='X' and board['8']=='X') or (board['3']=='X' and board['6']=='X' and board['9']=='X') or (board['1']=='X' and board['5']=='X' and board['9']=='X') or (board['3']=='X' and board['5']=='X' and board['7']=='X'):
        return("Player 1")
    elif (board['1']=='O' and board['2']=='O' and board['3']=='O') or (board['4']=='O' and board['5']=='O' and board['6']=='O') or (board['7']=='O' and board['8']=='O' and board['9']=='O') or (board['1']=='O' and board['4']=='O' and board['7']=='O') or (board['2']=='O' and board['5']=='O' and board['8']=='O') or (board['3']=='O' and board['6']=='O' and board['9']=='O') or (board['1']=='O' and board['5']=='O' and board['9']=='O') or (board['3']=='O' and board['5']=='O' and board['7']=='O'):
        return ("Player 2")
    else: return False
    
#Creates a function that prints the default board to the screen

def defaultBoard():
    print('  1' + '  |' + '  2' + '  |' +'  3')
    print('-----+-----+-----')
    print('  4' + '  |' +  '  5' + '  |'+'  6')
    print('-----+-----+-----')
    print('  7' + '  |' + '  8' + '  |'+'  9')
    
#Main Program
print("Welcome to Tic Tac Toe! The object of this game is to get three in a row. You play on a three by three game board.\n")
print("Player 1, you are X\n")
print("Player 2, you are O\n")
print("Rules: Players alternate placing Xs and Os on the game board until either opponent has three in a row, column, diagonally, or all nine squares are filled.")
print("Here are the positions on the board\n")
defaultBoard()
print("_____________________________________________________________________________________________________________________________________________________________")

i=0
p=1
while i<10:
    while True:
        try:
            moves=raw_input("Player "+str(p)+", make your move: ")
            # printBoard(theBoard)
        except:
            print("Invalid input. Try Again ")
            continue
        if moves=="1" or moves=="2" or moves=="3" or moves=="4" or moves=="5" or moves=="6" or moves=="7" or moves=="8" or moves=="9":
            break
        else:
            print("Invalid input. Try Again ")
            continue
    i=i+1
    if p==1:
        p=2
        theBoard[moves]="X"
        printBoard(theBoard)
        result= winCheck(theBoard)
        if result=="Player 1" or result=="Player 2":
            print("\nGame Over! "+ result + " YOU WIN!")
            break 
        if i==9:
            break
    elif p==2:
        p=1
        theBoard[moves]="O"
        printBoard(theBoard)
        result= winCheck(theBoard)
        if result=="Player 1" or result=="Player 2":
            print("\nGame Over! "+ result + " YOU WIN!")
            break 
        if i==9:
            break
        
    else:
        break


    
