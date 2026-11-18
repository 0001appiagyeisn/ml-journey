import sys


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    try:
        print(f"${(float(sys.argv[1]) / 15.5):.2f}")
    except ValueError:
        print("That's not an amount")