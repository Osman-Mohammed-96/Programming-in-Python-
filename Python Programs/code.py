#welcome message 
print("Welcome to the registration page") 
print("To register please follow the instructions below") 

print("Type in your username and password below") 
new_username = input("Please type in your username: ")
new_password = input("Please type in your password: ")

#Security check
security_password = input("Please enter in your password again: ") 

#Checking if password matches 
if(new_password != security_password):
    def Security():
        print("The password does not match!") 
    Security() 

#If password is correct after securitycheck 
print("Registration has been successfull") 
print("Your new features are waiting to be used!")
print("Please login to get started") 

#Login section of menu 
username = input("Please type in your username: ")
password = input("Please type in your password: ") 

#Check to see if login vredentials match with registered account details
if new_username == username and new_password == password:
    input("Access has been granted")
else:
    input("Access Denied!")