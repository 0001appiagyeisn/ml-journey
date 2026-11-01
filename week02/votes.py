votes = ["Ama","Kofi","Ama","Esi","Kofi","Ama"]

counts = {}
highest = votes[0]
for cand in votes:
    if cand in counts:
        counts[cand] += 1
    else:
        counts[cand] = 1
print(counts)

for cand in counts:
    if counts[cand] > counts[highest]:
        highest = cand

print(f"Winner: {highest} ({counts[highest]})")
