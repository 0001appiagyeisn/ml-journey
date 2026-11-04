def mean(data):
    return sum(data) / len(data) if data else 0

print(f"Mean: {mean([1500, 1800, 2000, 2200, 9000])}") 

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if  n % 2 == 1:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2

print(f"Median: {median([1500, 1800, 2000, 2200, 9000])}") 

def data_range(data):
    maximum = max(data)
    minimum = min(data)
    return maximum - minimum

print(f"Range: {data_range([31,33,30,32,34,29,31])}")
    
def mode(data):
    counts = {}
    highest = data[0]
    for num in data:
        if num in counts:
            counts[num] +=1
            
        else: 
            counts[num] = 1
    for num in counts:        
        if counts[num] > counts[highest]:
            highest = num
    return highest

sizes = [40, 42, 41, 42, 43, 42, 40, 44, 41, 42, 43, 41]
print(mode(sizes)) 
print(mode(["MTN", "AT", "MTN"])) 
        