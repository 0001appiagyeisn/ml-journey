
def scale(m,k):
    km = []
    for row in m:
        nr = []
        for x in row:
            nr.append(round(x * k))
        km.append(nr) 
    return km

print(scale([[1,2],[3,4]],2))
print(scale([[25, 20], [18, 10]], 1.1))

def add(a,b):
    addedmatrix = []
    for i in range(len(a)):
        rowmatrix = []
        for j in range(len(a[0])):
            
            added = a[i][j] + b[i][j]
            rowmatrix.append(added)
        addedmatrix.append(rowmatrix)
    return addedmatrix
Ama = [[12, 8, 5, 10], [15, 6, 7, 9], [10, 9, 4, 12]]
Esi = [[8, 5, 6, 4], [9, 7, 3, 6], [11, 4, 5, 8]]
print(add(Ama, Esi))

def dot(v, w):

    if len(v) != len(w):
        print("Lengths differ!")
        return None
    total = 0
    for i in range(len(v)):
        total = total + v[i] * w[i]
    return total

def mat_vec(m,v):
    matxvec = []
    for i in m:
        matxvec.append(dot(i,v))
    return matxvec

sales = [[12, 8, 5, 10], [15, 6, 7, 9], [10, 9, 4, 12]]
prices = [25, 20, 18, 10]
print(mat_vec(sales, prices))

def get_column(m,j):
    col = []
    for row in m:
        col.append(row[j])
    return col

def transpose(m):
    trans = []
    for j in range(len(m[0])):
        trans.append(get_column(m,j))
    return trans
print(transpose(sales))