#Welcome message 
print("Hello and welcome to the login screen of our system") 
print("Please login using your username and password") 

#Gathering user input 
username = input("Please enter your username: ") 
user_password = input("Please enter your password: ") 

#security check 
password = input("Please enter your password again: ") 
if(user_password == password): 
    #Making function for security check
    def Securitycheck():
        print("Login successfull:)") 
    #Using function        
    Securitycheck() 
if(user_password != password): 
    print("Login failed!!!!!")  