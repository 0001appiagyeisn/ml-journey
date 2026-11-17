from stats import mean, std_dev
import random
#Part 1: Simulate rolling a die 60,000 times and count the occurrences of each face
roll_times = 60000
counts = {}

for i in range(roll_times):
    ludo = random.randint(1,6)
    if ludo in counts:
        counts[ludo] += 1
    else:
        counts[ludo] = 1

for i in range(1,7):
    print(f"{i} was rolled {counts[i]} ({counts[i]/roll_times*100:.2f}%) ")

#Part 2: 3 attempts to roll a 6, Simulate 10000 attempts
count = 0
throws = 10000
for i in range(throws):
    for j in range(3):
        tryy = random.randint(1,6)
        if tryy == 6:
            count += 1
            break
print(f"P(No six in 3 rolls) = {1 - (count/throws):.3f}")

#Part 3: Roll 2 dice 3600 times count total from 2 to 12

rolls = 3600
total = []
t_counts = {}
for i in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    asum = dice1 + dice2
    if (asum) in t_counts:
        t_counts[asum] += 1
    else:
        t_counts[asum] = 1
    total.append(asum)
for j in range(2,13):
    print(f"{j}  {'#' * (int(t_counts[j]/20))}")
print(f"Mean of total rolls: {mean(total):.2f}")
print(f"Standard deviation of total rolls: {std_dev(total):.2f}")