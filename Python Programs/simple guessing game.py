#Welcome message 
print("Hello and welcome to the password guessing game") 
print("Please guess the correct password to unlock the vault") 
print("Enjoy and have fun!") 
#Gathering user input 
name = input("Please type in your name: ") 
print("Welcome to the game"+ name) 

#users options 
print("Please choose from one of the options below") 
print("1. Start Game") 
print("2. Exit Game") 

#User's input on decision 
option = input("Please enter from the following options above: ") 

#Output based on user's decision 
if (option == 1):
    print("The game has started") 
if (option == 2): 
    print("Exitting Game...")  
#Password guessing begins 
password = input("Please type in the correct password to win the game: ") 
if (password == "Programmer"):
    print("Congratulations you have guessed the correct password and have won the game!") 
else:
    print("Wrong guess, you lose!!!") 