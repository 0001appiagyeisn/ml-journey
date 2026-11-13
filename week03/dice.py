import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
if dice1 == dice2:
    print(f"Double! {dice1}")
else:
    print(f"Rolled {dice1} and {dice2}, total {total}")