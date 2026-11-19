sales = [[12, 8, 5, 10],
         [15, 6, 7, 9],
         [10, 9, 4, 12]]
print(sales[2])
print(f"Monday: Kelewele :{sales[1][3]}")
print(f"Shape {len(sales)}x{len(sales[0])}")

rtotal = 0
for i, row in enumerate(sales,1):
    for value in row:
        rtotal += value
    print(f"Row {i}: {rtotal}")
    rtotal = 0