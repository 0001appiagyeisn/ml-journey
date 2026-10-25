scores = [45,78,52,90,33,61]

smallest = scores[0]

for score in scores:
    if score < smallest:
        smallest = score

print(smallest)