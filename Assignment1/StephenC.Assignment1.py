firstname = raw_input("What is your first name?")
lastname = raw_input("What is your last name")
print(lastname + ", " + firstname)

name = raw_input("What is your name?")
age = input("How old are you?")
agehundred = 100 - age + 2019
print(name + ", " + "you will turn 100 in the year " + str(agehundred))

numberdivide = input("What is the number you want to divide?")
numberdivideby = input("What is the number you want to divide by?")
remainder = numberdivide % numberdivideby 
print(str(numberdivide) + " divided by " + str(numberdivideby) + " will leave a remainder of " + str(remainder))

word = raw_input("Give me a word: ")
amount = input("How many times do you want me to repeat it? ")
print(str(word) * amount)

length = input("What is the length of the rectangle? ")
width = input("What is the width of the rectangle? ")
perimeter = (length + length + width + width)
area = (length*width)
print("The perimeter of your rectangle is " + str(perimeter) + " units. The area is " + str(area) + " units squared")

diameter = input("What is the diameter of the circle? ")
radius = (diameter/2)
circumference = (3.14*radius)
area = (3.14*radius**2)
print("The circumference is " + str(circumference) + " units and the area is " + str(area) + " units squared ")

birthyear = input("What year were you born in? ")
age = (2019 - birthyear)
print("You are " + str(age) + " years old ")
