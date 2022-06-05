#Welcome message 
print("Hello and welcome to the registration page") 
print("Please answer the following questions to get registered") 

#Gathering user input 
new_username = input("Please type in your username: ") 
new_password = input("Please enter in your password: ") 

#Security check 
securitypassword = input("Please type in your password: ") 

#If security password does not match new password
if(new_password != securitypassword):
    #Creation of function for security check
    def Securitycheck(): 
        print("The current password does not match the existing password") 
        new_password = input("Please enter in the correct password: ") 
    securitypassword = input("Please type in your password again to confirm: ") 
    #calling function 
    Securitycheck() 

#Password is accurate and has passed the security check while password is correct
print("You have registered successfully!!") 
print("Your brand new features await you!") 
print("You may now login to access the features on your account") 

#User account login 
username = input("Please input your username: ") 
password = input("Please input your password: ") 

#Check to make sure login details are the same as registered account 
if new_username == username and new_password == securitypassword:
    input("Access has been granted :)") 
else: 
    input("Access has been denied!!!") 