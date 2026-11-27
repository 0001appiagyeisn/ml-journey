weather = ["rain", "dry", "dry", "rain", "dry", "rain", "dry", "dry", "rain", "dry"]
late = ["yes", "no", "no", "yes", "yes", "no", "no", "no", "yes", "no"]
count_rain = 0
both = 0
late_count = 0
for i in range(len(weather)):
    if weather[i] == "rain":
        count_rain += 1
        if late[i] == "yes":
            both +=1
    if late[i] == "yes":
        late_count += 1
print(f"Rain days: {count_rain}")
print(f"Late on rain days: {both}")
print(f"P(late | rain) = {(both/count_rain):.2f}")
print(f"P(late) = {(late_count/len(late)):.2f}")
