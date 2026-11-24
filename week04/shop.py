shop = {
 "name": "Auntie Ama's",
 "items": [
 {"food": "jollof", "price": 25},
 {"food": "waakye", "price": 20}
 ]
}
print(shop["name"])
print(shop["items"][0]["price"])
print( len(shop["items"]))

for item in shop["items"]:
    print(f"{item["food"]}: Ghc {item["price"]}")
