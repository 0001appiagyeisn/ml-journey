
items = []

while True:
    item = input("Enter an item (or type 'done' to finish): ").strip().capitalize()
    if item == "":
        print("Please enter a valid item.")
        continue
    if item.lower() == 'done':
        break
    items.append(item)

for i in range(len(items)):
    print(f"{i + 1}. {items[i]}")