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

print(grade(82))
print(grade(47)) 
print(grade(69))
print(grade(70))