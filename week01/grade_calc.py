#Ask user for the score
score = int(input("Enter your Score: "))

#grade calculator
if 100 >= score >=80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
elif score >= 0:
    print("Grade: F")
else:
    print("Score should be  0 - 100")