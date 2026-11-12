#using try and exception ask user for age
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please type a number like 19")
else:
    print(f"Next year youll be {age + 1} years")