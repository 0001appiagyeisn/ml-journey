names =["Ama","Kofi","Esi","Yaw"]
scores = [82,47,69,91]

highest_pos = 0
lowest_pos = 0

for i in range(len(names)):
    if scores[i] > scores[highest_pos]:
        highest_pos = i
    elif scores[i] < scores[lowest_pos]:
        lowest_pos = i

print(f"Highest: {names[highest_pos]} ({scores[highest_pos]})")
print(f"Lowest: {names[lowest_pos]} ({scores[lowest_pos]})")