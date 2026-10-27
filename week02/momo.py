balance = 200
pin = "4321"

asked_pin = input("Enter your pin: ")

if asked_pin == pin:
    amount = int(input("Enter amount to withdraw: "))
    print("New balance:", balance - amount)
    if amount > balance:
        print("Not enough balance")      
else:
    print("Wrong pin")