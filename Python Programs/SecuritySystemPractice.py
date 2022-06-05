#Basic passsord system 
#Lets the user login with the correct username and password

#Display welcome message  
print("Hello and welcome!") 
#gather user input 
reg_username = input("Please enter in the username: ") 
reg_password = input("Please enter in the password") 

#Added security 
security = input("Please type in your password") 

#if password is not the same as security check
if(security != reg_password ): 
    #Make function for security check 
    def securityCheck():
        print("The password you have entered does not match") 
        reg_password = input("Please type in the correct password") 
        security = input("Please type in your password") 
    #executing function
    securityCheck() 

#Once security check has been completed 
print("Login Suucessful!")
print("Your account awaits you") 
print("Have fun and enjoy!")  
