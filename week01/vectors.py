def add(v, w):
    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result

def scale(c, v):
    result = []
    for x in v:
        result.append(c * x)
    return result

print(add([-3,1], [1,2])) 
print(scale(2, [2,14])) 