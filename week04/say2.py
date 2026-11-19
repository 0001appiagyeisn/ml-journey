import cowsay
import sys

if len(sys.argv) == 3:
    if "trex" in sys.argv:
        cowsay.trex("Hello, " + sys.argv[2].capitalize())
    elif "cow" in sys.argv:
        cowsay.cow("Hello, " + sys.argv[2].capitalize())
    else:
        sys.exit("Animal must be cow or trex")
else:
    sys.exit("Usage: python say2.py ANIMAL NAME")
