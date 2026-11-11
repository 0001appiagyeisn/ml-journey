menu = {"jollof": 25, "waakye": 20," banku": 18, "kelewele": 10, "sobolo": 5}

orders = []

while True:
    order = input("Enter food: ").strip().lower()
    if order == "done":
        break
    if order not in menu:
        print("Sorry order not in menu")
        continue
    qty = int(input("Enter Quantity: "))
    orders.append({"food":order, "Quantity":qty})

print(orders)