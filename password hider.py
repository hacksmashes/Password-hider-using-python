import getpass

password=getpass.getpass(prompt="Enter the password : ")        # whatever u type in output window will not be visible to your eyes
if password == "python":               # U can give anything u want to set as a password        
    print("success")
else:
    print("Please type correctly...")   # if u type wrongly means this print statement will be print in the output window
