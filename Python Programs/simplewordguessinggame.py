#Word guessing game
#To win the game the user must guess the correct word
#3 options will be given to the user
#the correct word guessed allows the user to win

#Welcome message
print("Welcome to the word guessing game!") 
print("Please guess the correct word to win (:") 
print("Follow the instructions below and enjoy!") 

#Gathering users input 
word = input("Please enter the correct word to win: ") 

#checking to see if word matches the set word given 
if(word == "Developer"): 
    print("You have guessed the correct word, you win!") 
else: 
    print("Incorrect word, you lose!") 