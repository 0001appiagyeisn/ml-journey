import sys
from ghana import cedis, greet 

if len(sys.argv) < 3:
    sys.exit("Too few arguments. Usage: python filename Name Cash")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
else:
    try:
        print(f"{greet(sys.argv[1])} \nYou have {cedis(float(sys.argv[2]))}")
    except ValueError:
        print("Cash should be a number like 5000") 
