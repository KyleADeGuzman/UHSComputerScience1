import math

# 1
# Write a program that asks the user how many numbers they have (positive 
# integers only) and creates a list for them. Then, the program should scan the 
# list, tell them how many even and odd numbers the list contains,  and what 
# they are. 

NumList = []
Even = []
Odd = []

Number = int(input("Enter how many numbers in the list: "))
for i in range(1, Number + 1):
    value = int(input("Number Value %d : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even.append(NumList[j])
    else:
        Odd.append(NumList[j])

print("Element in Even List is : {0}".format(Even))
print("Element in Odd List is : {0}".format(Odd))

# ------------------------------------------------------------------------------

# 2
# Write a program that allows the user to enter a list of numbers and removes 
# duplicates from that list. The order does not matter. 

numlist=[]
number= int(input("Enter how many numbers in the list:"))
for i in range(1, number + 1):
    value = int(input("Number Value %d : " %i))
    numlist.append(value)
se = set()
unique = []
for x in numlist:
    if x not in se:
        unique.append(x)
        se.add(x)
print("I have removed all the duplicates from your list. You new list is: ")
print(unique)



# ------------------------------------------------------------------------------


#3) Write a program that asks the user to enter a list and then prints the list 
# in reverse order. 

n=0

colornumbers = input('How many colors do you have?:  ')
colorlist= []
while n < (colornumbers):
  colors= raw_input ("Enter the color: ")
  colorlist= colorlist + [colors]
  n=n+1
   
print colorlist[::-1]

# 4)  Write a program that asks the user to enter a list of numbers. The user 
# should then calculate the average and print it to the screen.
number = input('How many numbers are you looking to average: ')
total_sum = 0
for n in range(number):
    numbers = float(input('Enter number : '))
    total_sum += numbers
average = total_sum/number
print("Average of {0} numbers is : {1}" .format(number,average))
  
# 5
# Write a function that calculates the volume of a rectangular prism given 
# the length, width, and height. 

def rectPVolume(length,width,height):
    volume=length*width*height
    return volume

print rectPVolume(5,2,10)

# 6
# Write a function that finds the maximum of 3 numbers. 
def maximum(n1,n2,n3):
    total=max(n1, n2, n3)
    return total

print maximum(10,5,-3)


# 7
# Write a function that prints out a star pattern depending on 
# the parameter passed on to it. 

def star(rows):
    for j in range(rows-1,0,-1):
        print(''*(rows-j-1)+'* '*(j+1))
    for i in range(rows):
        print (''*(rows-i-1)+'* '*(i+1))
star(5)

# 8
# Ask the user to enter a list. Then, print out all the numbers in that list 
# that are less than 10. 

NumList = []
lesser = []

Number = int(input("Enter how many numbers in the list: "))
for i in range(1, Number + 1):
    value = int(input("Number Value %d : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] <10):
        lesser.append(NumList[j])
        
print "The numbers in your list that are less than 10 are: {0}".format(lesser)

# 9
#  Write a program that asks the user how many Fibonacci numbers to generate and
# then generates them. Use functions. Make sure to ask the user to enter the 
# number of numbers in the sequence to generate
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fibo = []
    elif num == 1:
        fibo = [1]
    elif num == 2:
        fibo = [1,1]
    elif num > 2:
        fibo = [1,1]
        while i < (num - 1):
            fibo.append(fibo[i] + fibo[i-1])
            i += 1
    return fibo
print(fibonacci())
input()

#10
#  Write a function for checking the speed of drivers. This function should 
# have one parameter: speed.
def speedcheck(speed):
    if speed <= 75:
        print "Ok"
    elif speed > 75:
        points=(speed/5)-15
        if points< 12:
            print ("You have " + str(points) + " points, drive better and slower!")
        elif points> 12:
            print str("You have " + str(points) + " points. License suspended")
    return speed

speedcheck(85)
