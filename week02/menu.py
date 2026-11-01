menu = {"jollof": 25, "waakye": 20, "banku": 18,"kelewele": 10}

order = input("What would you like to order? ").strip().lower()


if order in menu:
    print(f"The price of {order} is ${menu[order]}.")   

else:
    print(f"Sorry, we don't have {order} on the menu.")
    
    
