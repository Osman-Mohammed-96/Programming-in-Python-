#The cell cracker game involves the person being locked inside a cell
#The code needs to be guessed correctly to escape the cell 
#Different options are available to the user 
#Multiple codes to be added and user input is required 
#Print command, if statements needed 
print("Welcome to the cell cracker game!") 
print("You are currently stuck in a cell...") 
print("You must guess the code correctly in order to escape!")
print("Please follow the next steps in order to follow the instructions...")
name = input(("Please enter your name")) 
print("Welcome! " + name)  
print("You have 3 options to choose from " + name)  
print("Please select one of the following options below")
print("1. Stay in the cell") 
print("2. Escape the cell!") 
print("3. Exit Game") 
 
option = int(input("Please enter one of the options")) 
if option == 1:
    print("You are locked in the cell with no escape!!") 
if option == 2: 
    print ("You must guess the correct code to escaqpe the cell..!") 
if option == 3: 
    print("Exit Game...") 