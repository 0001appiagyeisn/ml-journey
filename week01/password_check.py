password = input("Create a password: ")

if len(password) < 8:
    print("Password must be at least 8 characters")
elif password.lower()== "password":
    print("Choose another password")    
else:
    print("Password strong, Created successfully")