import sys
from ghana import cedis
total = 0
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    try:
        for i in sys.argv[1:]:
            total += float(i)
        sys.exit(cedis(total))
    except ValueError:
        sys.exit("Only numbers, please like 500")
