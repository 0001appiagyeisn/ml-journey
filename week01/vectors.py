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

def dot(v, w):

    if len(v) != len(w):
        print("Lengths differ!")
        return None
    total = 0
    for i in range(len(v)):
        total = total + v[i] * w[i]
    return total
qty = [1, -1]
price = [1,1]

def mat_vec(matrix, v):
    result = []
    for row in matrix:
        result.append(dot(row, v))
    return result
    
M = [[1, 2], [3, 4]]
print(mat_vec(M, [1, 1]))

baskets = [[2, 1, 0], [1, 1, 1], [0, 3, 2], [4, 0, 1]]
prices = [10, 6, 15]
print(mat_vec(baskets, prices))


print(dot(qty, price)) 
print(add([-3,1], [1,2])) 
print(scale(2, [2,14])) 
print(length([3,4]))