menu = {"jollof":25,"waakye":20,"banku":18,"kelewele":10,"sobolo":5}

orders = []

while True:
    order = input("Food: ").lower().strip()
    if order == "done":
        break
    if order in menu:
        qty = int(input("Quantity:"))
        orders.append({"food":order,"qty":qty})
    else: 
        print(f"Sorry {order} not in menu: ")
total = 0
counts = {}
most_order = orders[0]
for i, order in enumerate(orders,1):
    food = order["food"]
    qty = order["qty"]
    price = menu[food] * qty
    print(f"{i}. {food} x{qty} = GHc {price}")
    total += price


    if food in counts:
        counts[food] += qty
    else:
        counts[food] = qty
for food in counts:
    if counts[food] > counts[most_order["food"]]:
        most_order = food

print(f"Total: Ghc {total}")

print(f"Most ordered: {most_order} ({counts[most_order]})")