import random

foods = ["jollof", "waakye", "banku", "kelewele"]
special = random.choice(foods)
print(f"Today's Special: {special}")
random.shuffle(foods)
print(foods)