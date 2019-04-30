print("Welcome to my restaurant.")
print("Here's the menu: ")
print("Sandwiches:                  Beverages: ")
print("")
print("Chicken sandwich: $5.25      Small drink: $1.00")
print("Beef sandwich: $6.25         Medium drink: $1.75")
print("Fish sandwich: $5.75         Large drink: $2.25")
print("")
print("The only side available is french fries: ")
print("Small fries: $1.00   Medium Fries: $1.50   Large fries: $2.00")
print("Ketchup is 25 cents per packet.")
print("")
swprice = 0
combo = 0

#-----
chicken = 0
beef = 0
fish = 0

smalldrink = 0
mediumdrink = 0
largedrink = 0

smallfries = 0
mediumfries = 0
largefries = 0
#-----

while True:
    sandwich = raw_input("Please choose a sandwich of your choice: ")
    if sandwich == "Chicken" or sandwich == "chicken":
        print("The price for the chicken sandwich is $5.25")
        chicken=+1
        swprice = 5.25
        break
    elif sandwich == "Beef" or sandwich =="beef":
        print("The price for the beef sandwich is $6.25")
        beef=+1
        swprice = 6.25
        break
    elif sandwich == "Fish" or sandwich == "fish":
        print("The price for the fish sandwich is $5.75")
        fish=+1
        swprice = 5.75
        break
    else:
        print("Please try again and input a valid sandwich choice.")
print("")

drink=0
while (drink!="Yes" and drink!="yes" and drink!="No" and drink!="no"):
    dprice = 0
    drink = raw_input("Would you like a beverage with your order? ")
    if drink == "No" or drink == "no":
        print("No beverage will be added to your order.")
        break
    elif drink == "Yes" or drink == "yes":
        combo =combo+ 1
        while True:
            size = raw_input("Which size beverage would you like? ")
            if size == "Small" or size == "small":
                smalldrink=+1
                print("The price for a small drink is $1.00 and has been added to your order.")
                dprice = swprice + 1.00
                break
            elif size == "Medium" or size == "medium":
                mediumdrink=+1
                print("The price for a medium drink is $1.75 and has been added to your order.")
                dprice = swprice + 1.75
                break
            elif size == "Large" or size == "large":
                largedrink=+1
                print("The price for a large drink is $2.25 and has been added to your order.")
                dprice = swprice + 2.25
                break
            else:
                print("Please enter a valid size and try again")
                
    else:
        print("Please enter yes or no and try again.")
print("")
while True:
    fryprice = 0
    fries = raw_input("Would you like fries with your order? ")
    if fries == "No" or fries == "no":
        print("No fries will be added to your order.")
        break
    elif fries == "Yes" or fries == "yes":
        combo =combo+ 1
        while True:
            frysize = raw_input("Which size fries would you like? ")
            
            if frysize == "Small" or frysize == "small":
                smallfries=+1
                print("The price for small fries is $1.00.")
                fryprice = dprice + 1.00
                frysize2 = raw_input("Would you like to upgrade from small to large size? ")
                if frysize2 == "No" or frysize2 == "no":
                    smallfries=+1
                    print("Size of fries will not be upgraded.")
                    fryprice = dprice + 1.00
                    break
                elif frysize2 != "Yes" and frysize2 != "yes":
                    print("Please enter a valid answer.")
                    continue
                elif frysize2 == "Yes" or frysize2 == "yes":
                    largefries=+1
                    print("Your fries have been upgraded.")
                    fryprice = dprice + 1.00
                    break
            elif frysize == "Medium" or frysize == "medium":
                mediumfries=+1
                print("The price for medium fries is $1.50 and has been added to your order.")
                fryprice = dprice + 1.50
                break
            elif frysize == "Large" or frysize == "large":
                largefries=+1
                print("The price for large fries is $2.00 and has been added to your order.")
                fryprice =  dprice + 2.00
                break
            else:
                print("Please enter a valid answer.")
    else:
        print("Please enter yes or no and try again.")
    break
print("")
while True:
    ketchupprice = 0
    ketchup = raw_input("How many ketchup packets would you like? ")
    try:
        ketchupinteger = int(ketchup)
        if ketchupinteger >= 0:
            ketchuptotal=(ketchupinteger*0.25)
            print(str(ketchup) + " packets have been added to your order.")
            ketchupprice = fryprice + ketchuptotal
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a number.")
print("")
print("Receipt: ")
print("")
if chicken == 1:
    print "You ordered 1 chicken sandwich:                                   $5.25"
    
if beef == 1:
    print "You ordered 1 beef sandwich:                                      $6.25"

if fish == 1:
    print "You ordered 1 fish sandwich:                                      $5.75"

if smalldrink == 1:
    print "You ordered 1 small drink:                                        $1.00"

if mediumdrink == 1: 
    print "You ordered 1 medium drink:                                       $1.75"

if largedrink == 1:
    print "You ordered 1 large drink:                                        $2.25"

if smallfries == 1:
    print "You ordered 1 small fries:                                        $1.00"

if mediumfries == 1:
    print "You ordered 1 medium fries:                                       $1.50"

if largefries == 1:
    print "You ordered 1 large fries:                                        $2.00"

if ketchupinteger !=0:
    print "You ordered " + str(ketchupinteger) +" ketchup packets:                                    $" + str(ketchuptotal)
    
if combo > 1:
    ketchupprice = ketchupprice - 1
    print("You've saved $1.00 off your order!")
else:
    print("No discount will be applied to your order.")
while True:
    total = ketchupprice*.07 + ketchupprice
    print("Your total comes to " + "$" + str(total))
    break
    
    
