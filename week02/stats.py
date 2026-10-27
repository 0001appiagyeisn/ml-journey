def mean(data):
    return sum(data) / len(data) if data else 0

print(mean([10, 20, 30, 60])) 
print(mean([4, 8, 6, 2])) 
print(mean([42, 38, 55, 47, 60, 58]))