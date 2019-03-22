from os import system, name 
  
from time import sleep 

def clear(): 
    
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 
  
print("  _    _      _ _       ")
sleep(.1)
print(" | |  | |    | | |      ")
sleep(.1)
print(" | |__| | ___| | | ___  ")
sleep(.1)
print(" |  __  |/ _ \ | |/ _ \ ")
sleep(.1)
print(" | |  | |  __/ | | (_) |")
sleep(.1)
print(" |_|  |_|\___|_|_|\___/ ")
sleep(.1)
print("                        ")

sleep(3) 
  
clear() 



    

  
print("Make sure to follow the directions")


answer = raw_input("Do you understand?  yes or no: ")
if answer == "yes":
    print("yes")
elif answer == "no":
    print("You said no")
    print(sleep(1000000))
else:
    print("Please enter yes or no.")
  
clear() 

    
  
print(" Loading .")
sleep(.1)
clear()
print(" Loading ..")
sleep(.1)
clear()
print(" Loading ...")
sleep(.1)
clear()
print(" Loading .... ")
sleep(.1)
clear()
print(" Loading .....")
sleep(.1)
clear()
print(" Loading ......")
sleep(.1)
clear()
print(" Loading .......")

sleep(2) 
  
clear() 
             
                        
#-------------------------------------------------------------------------------
# How to overcomplicate basic python code

print("----------------------------------------------")

#1a-----------------------
# Write a program that asks the user for the temperature in Fahrenheit and converts it to Celsius. [C = (5/9) * (F - 32)] **for the fraction, type it in as 5.0/9.0**
temperatureF= int(input("Input Temperature in F to find it in C: "))
temperatureC= (temperatureF-32)*5.0/9.0
print("The temperature of {0} degrees F is {1} degrees C." .format(temperatureF,temperatureC))
# -----------------------

print("----------------------------------------------")

#1b-----------------------
# Write a program that asks the user for the temperature in Celsius and converts it to Fahrenheit.
temperatureC= input("Input Temperature in C to find it in F: ")
temperatureF= temperatureC*9/5+32
print("The temperature of {0} degrees C is {1} degrees F.".format(temperatureC,temperatureF))
# -----------------------

print("----------------------------------------------")

#2-----------------------
# Write a program that asks the user to enter a number and then outputs whether that number is even or odd. 
number = input("Enter a number to check if it's odd or even: ")
if (number % 2) == 0:
   print("{0} is Even".format(number))
else:
   print("{0} is Odd".format(number))
# -----------------------
   
print("----------------------------------------------")  
   
#3-----------------------
# Write a Python program to check whether a letter of the alphabet is a vowel or consonant.
le = raw_input("Enter a letter to check if its a vowel or consonant: ")

if(le=='A' or le=='a' or le=='E' or le=='e' or le=='I'
 or le=='i' or le=='O' or le=='o' or le=='U' or le=='u'):
    print(le, "is a Vowel")
else:
    print(le, "is a Consonant")
# -----------------------

print("----------------------------------------------")

#4-----------------------
#  Write a Python program that asks the user to enter a month and outputs the number of days in that month.
print("Months (case sensitive): January, February, March, April, May, June, July, August, September, October, November, December")
month_name = raw_input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 
# -----------------------

print("----------------------------------------------")

#5-----------------------
# Write a Python program to display the astrological sign for a given date of birth. 
print("Days (numbers only) 1-31")
day = input("Input birthday for Zodiac sign: ")
print("Months (case sensitive): January, February, March, April, May, June, July, August, September, October, November, December")
month = raw_input("Input month of birth for Zodiac Sign: ")

if month == 'December':
	sign = 'Sagittarius' if (day < 22) else 'Capricorn'
	
elif month == 'January':
	sign = 'Capricorn' if (day < 20) else 'Aquarius'
	
elif month == 'February':
	sign = 'Aquarius' if (day < 19) else 'Pisces'
	
elif month == 'March':
	sign = 'Pisces' if (day < 21) else 'Aries'
	
elif month == 'April':
	sign = 'Aries' if (day < 20) else 'Taurus'
	
elif month == 'May':
	sign = 'Taurus' if (day < 21) else 'Gemini'
	
elif month == 'June':
	sign = 'Gemini' if (day < 21) else 'Cancer'
	
elif month == 'July':
	sign = 'Cancer' if (day < 23) else 'Leo'
	
elif month == 'August':
	sign = 'Leo' if (day < 23) else 'Virgo'
	
elif month == 'September':
	sign = 'Virgo' if (day < 23) else 'Libra'
	
elif month == 'October':
	sign = 'Libra' if (day < 23) else 'Scorpio'
	
elif month == 'November':
	sign = 'scorpio' if (day < 22) else 'Sagittarius'
	
print("Your Astrological sign is {0}" .format(sign))
# -----------------------

print("----------------------------------------------")

#6-----------------------
# Your Chinese Zodiac sign is derived from your birth year, according to the Chinese lunar calendar.
# Write a program that  accepts a year and outputs the Chinese Zodiac Sign associated with it.
year = input("Input year for Chinese Zodiac: ")

if (year - 2000) % 12 == 0:
    sign = 'Dragon'
    
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
    
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
    
elif (year - 2000) % 12 == 3:
    sign = 'sheep'
    
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
    
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
    
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
    
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
    
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
    
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
    
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
    
else:
    sign = 'Hare'

print("Your Zodiac sign {0}" .format(sign))
# -----------------------

print("----------------------------------------------")

#7-----------------------
# Write a Python program that asks the user to input a year and outputs to the user whether it is a leap year or not. 
year= input("Input year to check for leap year: ")


if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
# -----------------------

print("----------------------------------------------")

#8-----------------------
# Write a Python program that asks the user to enter 2 numbers and outputs the average. 
number = input('How many numbers are you looking to average: ')
total_sum = 0
for n in range(number):
    numbers = float(input('Enter number : '))
    total_sum += numbers
average = total_sum/number
print("Average of {0} numbers is : {1}" .format(number,average))
# -----------------------

print("----------------------------------------------")

#9-----------------------
# Write a Python program that asks the user to enter a linear equation (y=mx +b) by listing y, m, and b. Then solve this equation for x and output the result. 
print("To look for 'x' in the linear slope equation ")
y= input("Input y:")
m= input("Input m:")
b= input("Input b:")

x= (float(y)-float(b))/float(m)

print("Your eqauion is {0} = {1} x+ {2} and the solution is x = {3}".format(y,m,b,x))
# -----------------------

print("----------------------------------------------")

#10-----------------------
# Write a Python program that asks the user to enter an equation in standard form(Ax + By = C) by listing A, B, and C. Then find the x and y-intercepts. 
print("To look for 'x' and 'y' in the standard form ")
A= input("Input A:")
B= input("Input B:")
C= input("Input C:")

x= float(C)/float(A)
y= float(C)/float(B)

print("Your equation is {0} x {1} y = {2} . The x-intercept is {3} and y-intercept is {4}." .format(A,B,C,x,y))
# -----------------------

print("----------------------------------------------")

#-------------------------------------------------------------------------------

print("That is the end of assignment2.")
print("Assignment 3 will be coming soon.")

'''
100%
I love this! Superb coding skills and very creative!  
'''
