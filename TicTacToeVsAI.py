import random
import sys

print "Welcome to Tic Tac Toe!"
print "The board is set up like this: "
print "0|1|2"
print "3|4|5"
print "6|7|8"
print "Enter your first move, 0 through 8. (You are O's, the AI is X's)"


pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])

corners = [0, 2, 6, 8]
board = ["_", "_", "_", "_", "_", "_", " ", " ", " "]


turn = "PLAYER"

aiturn = 0

def printboard(turn, board, aiturn):
    print board[0] + "|" + board[1] + "|" + board[2]
    print board[3] + "|" + board[4] + "|" + board[5]
    print board[6] + "|" + board[7] + "|" + board[8]
    print "Turn: " + str(turn)
    if turn == 0:
        playermove(turn, board, aiturn)
    if turn == "AI":
        aiturn += 1
        aimove(turn, board, aiturn, corners)
    if turn == "PLAYER":
        playermove(turn, board, aiturn)


# Prompts the player to move
# I added some stuff that makes sure the input is legit. Thanks to Github user Kaligule for opening an issue.
def playermove(turn, board, aiturn):
    choice = raw_input("Enter a number 0-8: ")
    if choice.isdigit() == False:
        print "Keep it an integer, buddy."
        playermove(turn, board, aiturn)
    if int(choice) > 8 or int(choice) < 0:
        print "Make that a number between 0 and 8."
        playermove(turn, board, aiturn)
    if board[int(choice)] == 'X' or board[int(choice)] == 'O':
        print "That's already taken! Try again."
        playermove(turn, board, aiturn)
    else:
        board[int(choice)] = "O"
    turn = "AI"
    checkforwin(turn, board, aiturn)



def aimove(turn, board, aiturn, corners):
    alreadymoved = False
    completes = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])


    def cornerchoice(corners, board, alreadymoved):
        goodchoices = []
        if not alreadymoved:
            for i in corners:
                if board[i] == " " or board[i] == "_":
                    goodchoices.append(i)
            board[random.choice(goodchoices)] = "X"

    if aiturn == 1:
        if board[4] != "O":
            board[4] = "X"
            alreadymoved = True
        else:
            cornerchoice(corners, board, alreadymoved)
            alreadymoved = True
    else:
        for x in completes:
            # Offensive
            if board[x[0]] == "X" and board[x[1]] == "X" and board[x[2]] != "O":
                board[x[2]] = "X"
                alreadymoved = True
                break
            if board[x[1]] == "X" and board[x[2]] == "X" and board[x[0]] != "O":
                board[x[0]] = "X"
                alreadymoved = True
                break
            if board[x[0]] == "X" and board[x[2]] == "X" and board[x[1]] != "O":
                board[x[1]] = "X"
                alreadymoved = True
                break

        for x in completes:
            if alreadymoved == False:
                # Defensive
                if board[x[0]] == "O" and board[x[1]] == "O" and board[x[2]] != "X":
                    board[x[2]] = "X"
                    alreadymoved = True
                    break
                if board[x[1]] == "O" and board[x[2]] == "O" and board[x[0]] != "X":
                    board[x[0]] = "X"
                    alreadymoved = True
                    break
                if board[x[0]] == "O" and board[x[2]] == "O" and board[x[1]] != "X":
                    board[x[1]] = "X"
                    alreadymoved = True
                    break

    if not alreadymoved:
    
        if aiturn == 2 and board[4] == "O":
            cornerchoice(corners, board, alreadymoved)
        else:
            sides = [1, 3, 5, 7]
            humansides = 0
            for i in sides:
                if board[i] == "O":
                    humansides += 1
            if humansides >= 1:
                cornerchoice(corners, board, alreadymoved)
            else:

                goodchoices = []
                for i in sides:
                    if board[i] == " " or board[i] == "_":
                        goodchoices.append(i)
                if goodchoices == []:
                    cornerchoice(corners, board, alreadymoved)
                else:
                    board[random.choice(goodchoices)] = "X"

    turn = "PLAYER"
    checkforwin(turn, board, aiturn)


def checkforwin(turn, board, aiturn):
    for x in pairs:
        zero = board[x[0]]
        one = board[x[1]]
        two = board[x[2]]
        if zero == one and one == two:
            if zero == "X":
                print "AI wins."
                end()
            if zero == "O":
                print "Human wins. Did you cheat?"
                end()
        else:
            filledspaces = 0
            for i in range(8):
                if board[i] != " " and board[i] != "_":
                    filledspaces += 1
                if filledspaces == 8:
                    print "A draw! You will never win!"
                    end()

    printboard(turn, board, aiturn)


def end():
    print "Here is the final board."
    print board[0] + "|" + board[1] + "|" + board[2]
    print board[3] + "|" + board[4] + "|" + board[5]
    print board[6] + "|" + board[7] + "|" + board[8]
    sys.exit(0)


printboard(turn, board, aiturn)
