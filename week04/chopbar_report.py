from matrix import mat_mul, transpose

week = [
    [12, 8, 5, 10],
    [15, 6, 7, 9],
    [10, 9, 4, 12],
    [14, 7, 6, 11],
    [18, 10, 8, 15], 
    [20, 12, 9, 14]]
sell_cost = [
    [25, 15],
    [20, 11],
    [18, 10],
    [10, 5]]
days = ["Mon","Tue","Wed","Thu","Fri","Sat"]
food = ["jollof","waakye","banku","kelewele"]
week_profit = []
money = mat_mul(week, sell_cost)
best = 0 
print(f"Days    Takings     Costs    Profit")
for i, rows in enumerate(money):
    print(f"{days[i]}      {rows[0]}         {rows[1]}       {(rows[0]-rows[1])}")
    week_profit.append((rows[0]-rows[1]))
print(f"Week profit: GH₵ {sum(week_profit):,.2f}")

for j in range(len(week_profit)):
    if week_profit[j] > week_profit[best]:
        best = j

print(f"Best day: {days[best]} (GH₵ {week_profit[best]:,.2f})")

trans = transpose(week)
for i, plate in enumerate(trans):
    print(f" {food[i]} {sum(plate)}")
