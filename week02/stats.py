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
    