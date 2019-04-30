from random import*
easyguesses = 15
mediumguesses = 10
hardguesses = 5
easyrange = randint(1,100)
mediumrange = randint(1,300)
hardrange = randint(1,500)
print("Guessing Game: ")
while True:
    difficulty = raw_input("Please choose between easy, medium, or hard difficulty: ")
    if difficulty == "Easy" or difficulty == "easy":
        print("Your secret number is from 1 to 100 and you will have 15 guesses available.")
        while True:
            if easyguesses == 0:
                print("You have 0 guesses left, you lose :(")
                print("Your secret number was " + str(easyrange))
                break
            guess = int(input("Input an integer from 1 to 100: "))
            if guess > 100 or guess < 1:
                print("Please only input integers within the given range and try again.")
                continue
            elif guess < easyrange:
                easyguesses = easyguesses - 1
                print("You have " + str(easyguesses) + " guesses remaining.")
                print("Guess higher.")
                continue
            elif guess > easyrange:
                easyguesses = easyguesses - 1
                print("You have " + str(easyguesses) + " guesses remaining.")
                print("Guess lower.")
                continue
            else:
                print("You guessed the secret number, congrats!")
                break
        break
    if difficulty == "Medium" or difficulty == "medium":
        print("Your secret number is from 1 to 300 and you will have 10 guesses available.")
        while True:
            if mediumguesses == 0:
                print("You have 0 guesses left, you lose :(")
                print("Your secret number was " + str(mediumrange))
                break
            guess = int(input("Input an integer from 1 to 300: "))
            if guess > 300 or guess < 1:
                print("Please only input integers within the given range and try again.")
                continue
            elif guess < mediumrange:
                mediumguesses = mediumguesses - 1
                print("You have " + str(mediumguesses) + " guesses remaining.")
                print("Guess higher.")
                continue
            elif guess > mediumrange:
                mediumguesses = mediumguesses - 1
                print("You have " + str(mediumguesses) + " guesses remaining.")
                print("Guess lower.")
                continue
            else:
                print("You guessed the secret number, congrats!")
                break
        break
    if difficulty == "Hard" or difficulty == "hard":
        print("Your secret number is from 1 to 500 and you will have 5 guesses available.")
        while True:
            if hardguesses == 0:
                print("You have 0 guesses left, you lose :(")
                print("Your secret number was " + str(hardrange))
                break
            guess = int(input("Input an integer from 1 to 500: "))
            if guess > 500 or guess < 1:
                print("Please only input intgers within the given range and try again.")
                continue
            elif guess < hardrange:
                hardguesses = hardguesses - 1
                print("You have " + str(hardguesses) + " guesses remaining.")
                print("Guess higher.")
                continue
            elif guess > hardrange:
                hardguesses = hardguesses - 1
                print("You have " + str(hardguesses) + " guesses remaining.")
                print("Guess lower.")
                continue
            else:
                print("You guessed the secret number, congrats!")
                break
    else:
        print("Please enter a valid difficulty and try again.")
