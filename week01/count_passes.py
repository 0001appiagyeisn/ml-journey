scores = []

pass_mark = 50 

passes = 0

for pass_score in scores:
    if pass_score >= pass_mark:
        passes +=1

if len(scores) == 0:
    print("No scores were entered")
else:
    if passes == 1:
        word = "Student"
    else:
        word = "Students"
    print(f"{passes} {word} passed")

