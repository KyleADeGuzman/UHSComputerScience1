#worked with Kyle- Paolo

# 1. Create a Rock, Paper, Scissors game that allows you to play against the computer
import random

print("Hello! Welcome to the Rock Paper Scissors Program!")

isWin = False

while isWin == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")

    UserInput = int(input("What would you like to play?"))
    ComputerInput = random.randrange(1,3)

    if (UserInput == 1) and (ComputerInput == 1): 
        isWin = False
        print("It's a draw; you both played Rock!") 
        
    if (UserInput == 2) and (ComputerInput == 1):
        isWin == True
        print("You win! Paper covers rock!") # Paper beats Rock

    if (UserInput == 3) and (ComputerInput == 1): 
        isWin == True
        print("You lose! Rock blunts scissors!") # Rock beats scissor
        
    if (UserInput == 1) and (ComputerInput == 2): 
        isWin = True
        print("You lose! Paper covers rock!") # Paper beats Rock
        
    if (UserInput == 2) and (ComputerInput == 2): 
        isWin == False
        print("It's a draw; the computer played Paper!") # Draw

    if (UserInput == 3) and (ComputerInput == 2): 
        isWin == True
        print("You win! Scissors cut paper!") # Scissor beats Paper
        
    if (UserInput == 1) and (ComputerInput == 3): 
        isWin = True
        print("You win! Rock blunts scissors!") # Rock beats Scissors
        
    if (UserInput == 2) and (ComputerInput == 3):
        isWin == True
        print("You lose! Scissors cut paper!") # Scissor beats paper

    if (UserInput == 3) and (ComputerInput == 3):
        isWin == False
        print("It's a draw; the computer played Scissors!") # Draw
        



# 2. Create a Mad Libs game that allows the user to choose between 2 stories (You can create your own stories or find some interesting ones online; just make sure they are APPROPRIATE). 

# FYI:  Mad Libs are stories with blank spaces that a reader can fill in with their own words. The result is usually a funny (or strange) story.

# Mad Libs require:

# Words from the reader (for the blank spaces) 
# A story to plug the words into

# Prompt the user for input ( be specific, ask for verb, noun, adjective,animal noise, etc... ) 
# Print the entire Mad Libs story with the user's input in the right places. 



print "Welcome to Mad-Libs Lite"
print "------------------------"
print "Rules: "
print "1. Select a story"
print "2. Just Fill in the blanks with the correct word, either verb, noun, adjective,animal noise, etc. "
print "3. Then read it at the end"
print "------------------------"

while True:
    choice = input("Choose a story")
    
    if choice == 1:
        adjective1 = raw_input("Tell me an adjective, and click enter. ")
        noun1 = raw_input("Tell me a noun (plural), and click enter. ")
        noun2 = raw_input("Tell me another noun, and click enter. ")
        adjective2 = raw_input("Tell me an another adjective, and click enter. ")
        
        print "Roses are " + adjective1
        print noun1 + " are blue"
        print noun2 + " is " + adjective2
        print "And so are you!"
        break
        
    if choice == 2:
        adjective1 = raw_input("Tell me an adjective, and click enter. ")
        noun1 = raw_input("Tell me a noun (plural), and click enter. ")
        noun2 = raw_input("Tell me another noun, and click enter. ")
        adjective2 = raw_input("Tell me an another adjective, and click enter. ")
        
        print "Driving a car can be fun if you follow this " + adjective1 + " guide"
        print "When approaching a " + noun1 
        print "on the right, always blow your " + noun2 
        print "Before making a " + adjective2 + " turn."
        break


# 3. Write a FUNCTION that accepts the total price  and the square inch area of 
# a pizza pie as PARAMETERS, and then calculates the price per sq. in. 

import math

def pizza(inch):
    price = int(input("Enter Price:"))
    ans = price/inch
    print("The cost per square inch is $ %.2f"%ans )
  
pizza(18)


# 4. Write a FUNCTION that accepts an integer as a parameter and prints True if 
# it is within 10 of 100 or 200, and False if not. (Hint: abs(num) computes the
# absolute value of a number. )
def within_ten(n):
      return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print(within_ten(93))
print(within_ten(90))
print(within_ten(89))   
print(within_ten(195))


# 5. Create any function in python that you might use in math to help you solve a problem.
# Converts string to binary. Helps convery words to binary in computer engineering.
binary = []
def strBin(s_str):
	for s in s_str:
	    if s == ' ':
	        binary.append('00100000')
	    else:
	        binary.append(bin(ord(s)))
s_str = input("String: ")
strBin(s_str)

b_str = '\n'.join(str(b_str) for b_str in binary) 

print(b_str.replace('b',''))


# 6. Write a Python program to swap a  comma and a period in a string.
import re
def Replace(str1): 
    str1 = str1.replace(', ', 'third') 
    str1 = str1.replace('.', ', ') 
    str1 = str1.replace('third', '.') 
    return str1 
      
string = "32.054,23"
print(Replace(string)) 



# 7. Write a Python program to capitalize first and last letters of a string. 
def capitalize_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_last_letters("computer"))



# 8. Write a Python program that checks if a password is in the correct format:


import re 
password = raw_input ("Enter Password")
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
  
if flag ==-1: 
    print("Not a Valid Password") 

