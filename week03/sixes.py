import random

rolls = 1000000
sixes = 0
doubles = 0
for _ in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 6:
        sixes += 1
    if dice2 == dice1:
        doubles += 1
print(sixes, "sixes")
print("Share:", round(sixes / rolls, 3))
print(doubles, "doubles")
print("Share:", round(doubles / rolls, 3))