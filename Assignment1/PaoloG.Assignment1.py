#1
lastname= raw_input("What is your last name?: ")
firstname= raw_input("What is your firstname?: ")
print("Hello there! " + lastname + " , " + firstname)

#2
age= int(raw_input("What is your current age?: "))
cyear= int(raw_input("What is the current year?: "))
years100=int(100-age)
fyear=cyear+years100
year=str(fyear)
print("You will turn 100 in the year " + year)
print(cyear+years100)

#3 
divide1= input("What is the number you want to divide: ")
divide2= input("what is the number you want to be divided by: ")
divide3= divide1%divide2
print(str(divide1) + "  by " + str(divide2) + " and the remainder will be " + str(divide3))

#4
word= raw_input(" Type a word: ")
totalamount= input(" How many times do you want it to be repeated?: ")
print(str(word+ " ")*totalamount)

#5
lper= input("The length of the rectangle?: ")
wper= input("The area of the rectangle?: ")
per= (lper+wper)*2
area= (lper*wper)
print ("The Perimeter of the rectangle is " + str(per) + " units. The area is " +str(area) + " units sq.")

#6
diameter= input("What is the diameter?: ")
radius= (diameter/2)
circumference= (2*3.14*radius)
AREA6= (radius**2*3.14)
print(" The circumference is " + str(circumference) + " units and the area is "+ str(area) + " units sq.")

#7
YearOfBirth= input("What is the year were you born")
YearAge=(2019-YearOfBirth)
print("You were born on " + str(YearOfBirth) + " and you are probably " + str(YearAge) + " years old. ")
