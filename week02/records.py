students = [
    {"name": "Ama", "score": 82},
    {"name": "Kofi", "score": 47}, 
    {"name": "Esi","score": 69}
    ]
pas = 0

def grade(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
       return "C"
    if score >= 50:
        return "D"
    return "F"



for student in students:
    if student["score"] >= 50:
        pas += 1
    print(f"{student["name"]}: {student["score"]} ({grade(student["score"])})")
print(f"Passed: {pas} of {len(students)}")
