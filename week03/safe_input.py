def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Type a whole number, like 3")

q = get_int("Quantity: ")
print(q * 25)

def get_int_between(prompt,low,high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <=high:
                return value
            else:
                print(f"Between {low} and {high} please")
        except ValueError:
            print(f"Enter a whole number between {low} and {high} please")

score = get_int_between("Score: ", 0, 100)
print(f"Saved {score}")
    