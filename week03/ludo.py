
import random

roll_times = 6000
counts = {}

for i in range(roll_times):
    ludo = random.randint(1,6)
    for j in range(1,7):
        if ludo in counts:
            counts[j] += 1
        else:
            counts[j] = 1
print(counts)


