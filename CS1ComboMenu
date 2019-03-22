import datetime

import math

from os import system, name 

from time import sleep


def clear(): 
    
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')  
        
clear()
# ------
## Text menu in Python-----------------------------------------------------------------------
sandwich = 0
chicken = 0
beef = 0
fish = 0

beverage = 0
bsmall = 0
bmedium = 0 
blarge = 0

frenchfries = 0
fsmall = 0
fmedium = 0 
flarge = 0
fmega = 0

discounts = 0


def print_foodmenu():      
    print 30 * "-" , "SANDWICH MENU" , 30 * "-"
    print "1. Chicken: $5.25"
    print "2. Beef: $6.25"
    print "3. Fish: $5.75 "
    print 67 * "-"
  
def print_drinkmenu():
    print 30 * "-" , "DRINK SIZES" , 30 * "-"
    print "1. Small: $1.00 "
    print "2. Medium: $1.75 "
    print "3. Large: $2.25 "
    print 67 * "-"
    
def print_frenchfrymenu():
    print 30 * "-" , "FRENCH FRY SIZES" , 30 * "-"
    print "1. Small: $1.00 "
    print "2. Medium: $1.50 "
    print "3. Large: $2.00 "
    print 67 * "-"

def print_saucemenu():
    print 30 * "-" , "KETCHUP PER PACKET" , 30 * "-"
    print "$0.25 PER KETCHUP PACKET"
    print 67 * "-"
    
    

# ------------------------------Sandwich------------------------------

loop=True      
while loop:
    print ("Hello there, customer! Please select your order correctly and carefully.")

    print ("OFFICIAL NOTICE: Taxes will be applied at the end of the order. ")

    print 75*"-"

    print ("Deal: Buy any selection of sandwich meals, any french fry sizes, and any beverage sizes and recieve a $1.00 discount for your entire order.")
    print_foodmenu()
    choice = raw_input("Enter your choice [1-3]: ")
     
    if choice=="1": #Chicken option
        print 30 * "-"
        print "Chicken Sandwich selected"
        chicken=+1
        sleep(2)
        loop=False 
    elif choice=="2": #Beef option
        print 30 * "-"
        print "Beef Sandwich selected"
        beef=+1
        sleep(2)
        loop=False 
    elif choice=="3": #Fish option
        print 30 * "-"
        print "Fish Sandwich selected"
        fish=+1
        sleep(2)
        loop=False 
    else:
        print 30 * "-"
        print("Wrong option selection.")
        sleep(1)
        clear()
        
#---------------------------------------------------------------------

clear()
    
# ------------------------------Beverage------------------------------
loop=True
answer=""
while (answer!="YES" and answer!="NO"):
    answer = raw_input("Would you like a beverage?  yes or no: ").upper()

    if answer == "YES":
        clear()
        beverage=+1
        discounts=discounts+1
        while loop:      
            print_drinkmenu()   
            choice = raw_input("Enter your choice [1-3]: ")
     
            if choice=="1": #Small option
                print 30 * "-"
                print "Small Beverage selected"
                bsmall=+1
                sleep(2)
                loop=False 
            
            elif choice=="2": #Medium option
                print 30 * "-"
                print "Medium Beverage selected"
                bmedium=+1
                sleep(2)
                loop=False 
            
            elif choice=="3": #Large option
                print 30 * "-"
                print "Large Beverage selected"
                blarge=+1
                sleep(2)
                loop=False 
            else:
                print 30 * "-"
                print("Wrong option selection. ")
                sleep(1)
                clear()
        
    elif answer == "NO":
        print 30 * "-"
        print("No beverage added")
        sleep(2)
        loop=False
    
    else:
        print 30 * "-"
        print("Please enter yes or no.")
        sleep(1)
        clear()
        
#---------------------------------------------------------------------

clear()   
  
# ------------------------------French Fries------------------------------
answer=""
while (answer!="YES" and answer!="NO"):
    answer = raw_input("Would you like a French Fries?  yes or no: ").upper()

    if answer == "YES":
        clear()
        loop=True      
        frenchfries=+1
        discounts=discounts+1
        while loop:      
            print_frenchfrymenu()   
            choice = raw_input("Enter your choice [1-3]: ")
     
            if choice=="1": #Small option
                clear()
                print_frenchfrymenu()
                megaA=""
                while (megaA!="YES" and megaA!="NO"):
                    clear()
                    print_frenchfrymenu()
                    megaA = raw_input("Do you want to upgrade to MEGA SIZE? yes or no. ").upper()
                    if megaA == "YES":
                        print 30 * "-"
                        print "Mega Fries selected"
                        fmega=+1
                        sleep(2)
                        loop=False
                    elif megaA == "NO":
                        print 30 * "-"
                        print "Small fries selected"
                        fsmall=+1
                        sleep(2)
                        loop=False
                    else:
                        print 30 * "-"
                        print("Wrong option selection.")
                        sleep(1)
                        clear()
            
                
            elif choice=="2": #Medium option
                print 30 * "-"
                print "Medium Fries selected"
                fmedium=+1
                sleep(2)
                loop=False 
            
            elif choice=="3": #Large option
                print 30 * "-"
                print "Large Fries selected"
                flarge=+1
                sleep(2)
                loop=False
            
            else:
                print 30 * "-"
                print("Wrong option selection.")
                sleep(1)
                clear()
        
    elif answer == "NO":
        print 30 * "-"
        print("No French Fries were added")
        sleep(2)
        loop=False
    else:
        print 30 * "-"
        print("Please enter yes or no.")
        sleep(1)
        clear()

#----------------------------------------------------------------------------

clear()
    
# ------------------------------Ketchup Packets------------------------------

number=None
while number is None:
        print_saucemenu()
	user_number = raw_input ("Enter the amount of ketchup packets: ")
	try:
		val = int(user_number)
		if(val > -1):
        		ketchup=val*0.25
        		print 30 * "-"
        		print("{0} Ketchup Packets have been added".format(user_number))
        		sleep(2)
        		clear()
        		number=False
		else:
			print("Enter a Positive Number Only ") 
			sleep(1)
			clear()
	except ValueError:
		print("Enter a Integer Only ")
		sleep(1)
		clear()
		
#--------------------------------------------------------------------

clear()
    
# ------------------------------Reciept------------------------------

print datetime.datetime.today().strftime('%Y-%m-%d')
print (30 * "-" )

if chicken == 1:
    print "You have order 1 chicken                                      ~$5.25"
        
if beef == 1:
    print "You have order 1 beef                                         ~$6.25"
        
if fish == 1:
    print "You have order 1 fish                                         ~$5.75"
        
if bsmall == 1:
    print "You have order 1 small beverage                               ~$1.00"
        
if bmedium == 1: 
    print "You have order 1 medium beverage                              ~$1.75"
        
if blarge == 1:
    print "You have order 1 large beverage                               ~$2.25"
        
if fsmall == 1:
    print "You have order 1 small fries                                  ~$1.00"
        
if fmedium == 1:
    print "You have order 1 medium fries                                 ~$1.50"
        
if flarge == 1:
    print "You have order 1 large fries                                  ~$2.00"
    
if fmega == 1:
    print "You have order 1 mega fries                                   ~$2.00"
    
if val !=0:
    print "You have ordered {0} Ketchup Packets                            ~${1}".format(user_number,format(math.floor(ketchup * 100) / 100, ',.2f'))

#------------------------------------------------------------------------
#print ("$"+ str(total))
total = 0
sub = 0


sub = chicken*5.25 + beef*6.25 + fish*5.75 + bsmall*1.00 + bmedium*1.75 + blarge*2.25 + fsmall*1.00 + fmedium*1.50 + flarge*2.00 + fmega*2.00 + ketchup


tax = sub * 0.07
total = sub + tax

dis=0
if  discounts > 1:
    total=total-1
    dis=+1
    print "You saved $1.00 on your order. "
else:
    print "No discounts were applied to your order."


#option B
# print "subtotal = {0}".format(sub)
# print "total = {0}".format(total)


# OPTION A
print (38 * " " + 30 * "-" )
print  "                                          SUBTOTAL:           ~${0}".format(format(math.floor(sub * 100) / 100, ',.2f'))
print  "                                          DISCOUNT            ~${0}-".format(format(math.floor(dis * 100) / 100, ',.2f'))
print  "                                          TAX                 ~${0}".format(format(math.floor(tax * 100) / 100, ',.2f'))
print (38 * " " + 30 * "-" )
print  "                                                  TOTAL:      ~${0}".format(format(math.floor(total * 100) / 100, ',.2f'))
print(" ________  ____  _____     _____   ___   ____  ____   ")
print("|_   __  ||_   \|_   _|   |_   _|.'   `.|_  _||_  _|  ")
print("  | |_ \_|  |   \ | |       | | /  .-.  \ \ \  / /    ")
print("  |  _| _   | |\ \| |   _   | | | |   | |  \ \/ /     ")
print(" _| |__/ | _| |_\   |_ | |__' | \  `-'  /  _|  |_     ")
print("|________||_____|\____|`.____.'  `.___.'  |______|    ")

print("If the whole menu does not show, adjust the size of the run window and try again.")

exit= raw_input ('')

