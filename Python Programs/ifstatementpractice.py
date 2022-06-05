#practicing using if statements 

#User input
print("Please enter the correct password to enter") 
username = input("Please enter your username: ")
your_password = input("Please enter your password: ") 

#Security check
password = input("Please enter your password again: ") 

#cross check to see if password matches original password 
if(your_password == password): 
    print("Access Granted") 
else:
    print("Access Denied") 
