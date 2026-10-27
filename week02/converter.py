def to_dollars(cedis,rate):
    return round(cedis / rate,2)

print(to_dollars(150, 15.5))
print(to_dollars(1000, 15.5))