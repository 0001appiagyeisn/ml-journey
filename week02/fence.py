def fence_cost(metres,price):
    return metres * price
    

def perimeter(length,width):
    return (2 * length) + (2 * width)

total_m = perimeter(30,20)
cost = fence_cost(total_m,12)


print(f"Fence: {total_m} m, Cost Ghc {cost}")
