#security system for users 
#only let's the user in with the proper credentials 
#Double verification added for extra security 

#Welcome message 
print("Hello and welcome to the menu") 
print("Please enter the correct details to enter in to the system") 
print("Follow the instructions below")

#User input required
user_ID = input("Please enter your user ID: ")
username = input(str("Please type in your username: ")) 
user_password = input("Please enter in your password: ") 

#security check 
password = input("Please type in your password again: ") 
user = input("Please re-enter your username: ") 
new_ID = input("Please type in your ID again: ") 

#code to be added here soon 

if user_password == password: 
    print("Congratulations you have logged into the system sucessfully") 
    print("Your account is waiting for you")
    print("Have fun and enjoy!") 

if user_password != password:
    print("Unauthorised login attempted") 
    print("Login denied!!!")  