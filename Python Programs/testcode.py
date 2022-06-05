#welcome message 
print("Hello and welcome to the game!!!")
print("Please follow the instructions below to get started!") 

#input from user based on instructions 
name = input("Please enter your name: ") 
print("Welcome " + name) 
print("You have now entered the game" + name) 
print("Have fun and follow the steps as required!!!" + name) 

#options user has 
print("Select one of the options below") 
print("1. Start game") 
print("2. Exit game") 

#users input 
option = input("Please type in the option you would like to choose: ") 

#Action based on users choice 

if option == 1: 
    print("The game has started!!") 
if option == 2:
    print("Exitting Game...")
else:
    print("Invalid response!!") 

