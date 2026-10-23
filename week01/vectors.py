import math


def add(v, w):
    
    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result

def length(v):
   total = 0
   for x in v:
       total = total + x ** 2
   return math.sqrt(total)

def scale(c, v):
    result = []
    for x in v:
        result.append(c * x)
    return result

print(add([-3,1], [1,2])) 
print(scale(2, [2,14])) 
print(length([3,4]))