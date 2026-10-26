num_students = int(input("Enter the number of students: "))

names = []
scores = []
grades = []
passed = 0
for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}.: ")
    score = int(input(f"Enter the score of student {i + 1}.: "))
    while 100 < score or score < 0:
        score = int(input(f"Enter the score of student within (0-100) {i + 1}.: "))

    
    names.append(name)
    scores.append(score)


    if 100 >= score >= 80:
        grade = "A"
    elif score >=70:
        grade = "B"
    elif score >=60:
        grade = "C"
    elif score >=50:
        grade = "D"
    else: 
        grade = "F"

    grades.append(grade)

    if score >= 50:
        passed +=1
    
    
biggest = 0
smallest = 0

for i in range(num_students):
    if scores[i] > scores[biggest]:
        biggest = i
    elif scores[i] < scores[smallest]:
        smallest = i

for i in range(num_students):
    print(f"{names[i]} ({grades[i]})")

print(f"Average: {(sum(scores))/num_students:.2f}")
print(f"Highest: {names[biggest]} {scores[biggest]}")
print(f"Lowest: {names[smallest]} {scores[smallest]}")
print(f"Passed: {passed} of {num_students}")
    