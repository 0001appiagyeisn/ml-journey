score = [45, 78, 52, 90, 33, 61]

backwards = []

for i in range(len(score)-1,-1,-1):
    backwards.append(score[i])

print(backwards)
print(score[::-1])