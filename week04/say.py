import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python say.py NAME")

cowsay.cow("hello, "+ sys.argv[1])