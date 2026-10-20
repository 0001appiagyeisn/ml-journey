#Ask for total bill amount and number of people
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))

#each share
each_share = total_bill / num_people

print(f"Everyone is paying GHS{each_share:.2f} each")