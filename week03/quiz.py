import random
from safe_input import get_int

correct = 0
missed = []
operator = ["+" , "-"]

for i in range(5):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    opp = random.choice(operator)

    user_ans = get_int(f"{i+1}. {num1} {opp} {num2} = ")

    if opp == "+":
        ans = num1 + num2
    else:
        ans = num1 - num2

    if ans == user_ans:
        correct += 1
        print("Correct!")
    else:
        missed.append(f"{i+1}. {num1} {opp} {num2} = {ans} ")
        print(f"Wrong, it's {ans}")

print(f"Score: {correct}/5")
for miss in missed:
    print(f"Missed: {miss}")
