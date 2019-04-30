1 a:
farenheit = input("What is the degrees in Farenheit? ")
celsius = (5.0/9.0)*(farenheit - 32)
print("The temperature of " + str(farenheit) + " degrees F is " + str(celsius) + " degrees C ")

b:
celsius = input("What is the degress in celsius? ")
farenheit = (celsius * 9.0/5.0) + 32
print("The temperature of " + str(celsius) + " degrees C is " + str(farenheit) + " degrees F ")

2
oddoreven = int(input("Input a number: "))
modulo = oddoreven % 2.0
if modulo > 0:
    print("The number " + str(oddoreven) + " is odd.")
else:
    print("The number " + str(oddoreven) + " is even.")

3
letter = raw_input("Input a letter of the alphabet: ")
if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print("The letter " + str(letter) + " is a vowel.")
else:
    print("The letter " + str(letter) + " is a consonant.")

4
while True:
    month = raw_input("Input the name of the month: ")
    if month == "January":
        print("There are 31 days in January.")
        break
    if month == "February":
        print("There are 28 days in February.")
        break
    if month == "March":
        print("There are 31 days in March.")
        break
    if month  == "April":
        print(" There are 30 days in April.")
        break
    if month == "May":
        print("There are 31 days in May.")
        break
    if month == "June":
        print(" There are 30 days in June.")
        break
    if month == "July":
        print("There are 31 days in July.")
        break
    if month == "August":
        print("There are 31 days in August.")
        break
    if month == "September":
        print("There are 30 days in September.")
        break
    if month == "October":
        print("There are 31 days in October.")
        break
    if month == "November":
        print("There are 30 days in November.")
        break
    if month == "December":
        print("There are 31 days in December.")
        break
    else:
        print("Please input a valid month. Try again.")

#5
while True:
    month = raw_input("Please input the month you were born in: ")
    day = int(input("Please input the day you were born on: "))
    if month == "January" and day >= 20 and day <= 31:
        print("You're an Aquarius.")
        break
    elif month == "February" and day <= 18 and day >= 1:
        print("You're an Aquarius.")
        break
    elif month == "February" and day >= 19 and day <= 28:
        print("You're a Pisces.")
        break
    elif month == "March" and day <= 20 and day >= 1:
        print("You're a Pisces.")
        break
    elif month == "March" and day >= 21 and day <= 31:
        print("You're an Aries.")
        break
    elif month == "April" and day <= 19 and day >= 1:
        print("You're an Aries.")
        break
    elif month == "April" and day >= 20 and day <= 30:
        print("You're a Taurus.")
        break
    elif month == "May" and day <= 20 and day >= 1:
        print("You're a Taurus.")
        break
    elif month == "May" and day >= 21 and day <= 31:
        print("You're a Gemini.")
        break
    elif month == "June" and day <= 20 and day >= 1:
        print("You're a Gemini.")
        break
    elif month == "June" and day >= 21 and day <= 30:
        print("You're a Cancer.")
        break
    elif month == "July" and day <= 22 and day >= 1:
        print("You're a Cancer.")
        break
    elif month == "July" and day >= 23 and day <= 31:
        print("You're a Leo.")
        break
    elif month == "August" and day <= 22 and day >= 1:
        print("You're a Leo.")
        break
    elif month == "August" and day >= 23 and day <= 31:
        print("You're a Virgo.")
        break
    elif month == "September" and day <= 22 and day >= 1:
        print("You're a Virgo.")
        break
    elif month == "September" and day >= 23 and day <= 30:
        print("You're a Libra.")
        break
    elif month == "October" and day <= 22 and day >= 1:
        print("You're a Libra.")
        break
    elif month == "October" and day >= 23 and day <= 31:
        print("You're a Scorpio.")
        break
    elif month == "November" and day <= 21 and day >= 1:
        print("You're a Scorpio.")
        break
    elif month == "November" and day >= 22 and day <= 30:
        print("You're a Sagittarius.")
        break
    elif month == "December" and day <= 21 and day >= 1:
        print("You're a Sagittarius.")
        break
    elif month == "December" and day >= 22 and day <= 31:
        print("You're a Capricorn.")
        break
    elif month == "January" and day <= 19 and day >= 1:
        print("You're a Capricorn.")
        break
    else:
        print("Please input a valid Month or date. Try again.")

6
while True:
    year = int(input("Input the year you were born in: "))
    if year == 2008 or year == 1996 or year == 1984 or year == 1972 or year == 1960:
        print("You're a Rat.")
        break
    elif year == 2009 or year == 1997 or year == 1985 or year == 1973 or year == 1961:
        print("You're an Ox.")
        break
    elif year == 2010 or year == 1998 or year == 1986 or year == 1974 or year == 1962:
        print("You're a Tiger.")
        break
    elif year == 2011 or year == 1999 or year == 1987 or year == 1975 or year == 1963:
        print("You're a Rabbit.")
        break
    elif year == 2012 or year == 2000 or year == 1988 or year == 1976 or year == 1964:
        print("You're a Dragon.")
        break
    elif year == 2013 or year == 2001 or year == 1989 or year == 1977 or year == 1965:
        print("You're a Snake.")
        break
    elif year == 2014 or year == 2002 or year == 1990 or year == 1978 or year == 1966:
        print("You're a Horse.")
        break
    elif year == 2015 or year == 2003 or year == 1991 or year == 1979 or year == 1967:
        print("You're a Goat.")
        break
    elif year == 2016 or year == 2004 or year == 1992 or year == 1980 or year == 1968:
        print("You're a Monkey.")
        break
    elif year == 2017 or year == 2005 or year == 1993 or year == 1981 or year == 1969:
        print("You're a Rooster.")
        break
    elif year == 2018 or year == 2006 or year == 1994 or year == 1982 or year == 1970:
        print("You're a Dog.")
        break
    elif year == 2019 or year == 2007 or year == 1995 or year == 1983 or year == 1971:
        print("You're a Pig.")
        break
    else:
        print("PLease input a valid year. Try again.")

7
year = int(input("Please input a year to determine if it's a leap year: "))
if(year % 4.0 == 0 and year % 100.0 == 0 or year % 400.0 == 0):
    print("The year " + str(year) + " is a leap year.")
else:
    print("The year " + str(year) + " is not a leap year.")

8
numberone = int(input("Input a number: "))
numbertwo = int(input("Input another number: "))
average = (numberone + numbertwo) / 2.0
print("The average between the two numbers is " + str(average) + ".")

9
print("Solving a slope problem.")
y = int(input("Input your y value: "))
m = int(input("Input your m value: "))
b = int(input("Input your b value: "))
slope = (y - b) / m
print("Your equation is " + str(y) + " = " + str(m) + " x + " + str(b) + ", and the solution is x = " + str(slope) + "."  )

10
print("Solving a standard form problem.")
while True:
    a = int(input("Input your A value: "))
    b = int(input("Input your B value: "))
    c = int(input("Input your C value: "))
    if c > a and c > b:
        xintercept = c/a
        yintercept = c/b
        print("Your equation is " + str(a) + "x + " + str(b) + "y = " + str(c) + ". The x-intercept is " + str(xintercept) + " and the y-intercept is " + str(yintercept) + ".")
        break
