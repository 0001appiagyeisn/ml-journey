shirts = ["white","blue"]
trousers = ["black","brown","khaki"]
counts = 0
for shirt in shirts:
    for trouser in trousers:
        print(f"{shirt} shirt + {trouser} trousers")
        counts += 1
print(f"{counts} outfits")