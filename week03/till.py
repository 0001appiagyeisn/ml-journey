#Menu
menu = {"jollof": 25, "waakye": 20," banku": 18, "kelewele": 10, "sobolo": 5}

#Orders and quantity ordered
orders = []

#Loop to take orders and quantity
while True:
    order = input("Enter food: ").strip().lower()
    if order == "done":
        break
    if order not in menu:
        print("Sorry order not in menu")
        continue
    qty = int(input("Enter Quantity: "))
    orders.append({"food":order, "Quantity":qty})

#dict for orders and total quantity made
qty_ord = {}
totals = 0
most = orders[0]["food"]
for i, o in enumerate(orders,1):
    food = o["food"]
    qtyy = o["Quantity"]
    total = menu[food] * qtyy
    
    if food in qty_ord:
        qty_ord[food] += qtyy
    else:
        qty_ord[food] = qtyy
    print(f"{i}. {food} x{o["Quantity"]} = Ghc {total}")
    totals += total

for food in qty_ord:
    if qty_ord[food] > qty_ord[most]:
        most = food

    if totals >= 100:
        discount = 0.1 * totals


print(qty_ord)
print(f"Totals: Ghc {totals:.2f}")
print(f"Discount: Ghc {discount:.2f}, Pay Ghc {(totals - discount):.2f}")
print(f"Most ordered: {most} ({qty_ord[most]})")
