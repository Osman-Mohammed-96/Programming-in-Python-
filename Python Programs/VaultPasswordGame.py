#make a game where user enters a word to access secret vault,
#if word is not equal to password
#access denied
#else access granted
#fixed word is developer 

print("Welcome to the vault")
print("Please enter the correct word in order to access the vault!") 
word = input("Please enter the correct word to access the vault: ")
if word != "Developer":
    print("Access Denied!") 
else:
    print("Access Granted") 

