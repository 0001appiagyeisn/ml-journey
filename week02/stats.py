import math 

def mean(data):
    return sum(data) / len(data) if data else 0
 

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if  n % 2 == 1:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2



def data_range(data):
    maximum = max(data)
    minimum = min(data)
    return maximum - minimum


    
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


        

def variance(data):
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)


def std_dev(data):
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return math.sqrt(total / len(data))



