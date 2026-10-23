name = "Appiagyei Gyamfi"
pin = "0357"

login_name = input("Enter your name: ").lower().strip()
login_pin = input("Enter your pin: ").strip()

if login_name == name.lower() and login_pin == pin:
    print(f"Welcome {name}! ") 

else:
    print("Login failed. Please check your name and pin.")
