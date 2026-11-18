import sys

print(f"{len(sys.argv)} words")
for i,word in enumerate(sys.argv):
    print(f"{i} {word}")