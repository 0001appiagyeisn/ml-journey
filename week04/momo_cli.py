from multiprocessing import Value
import sys
from stats import mean,std_dev,median


if len(sys.argv) < 2:
    sys.exit("Usage: python momo_cli.py 23 31 ...")
else:
    try:
        amounts = []
        for i in sys.argv[1:]:
            amounts.append(float(i))
        meann = mean(amounts)
        biggest = max(amounts)
        sd = std_dev(amounts)
        z = abs((biggest - meann)/sd)
        print(f"Days :    {len(amounts)}")
        print(f"Total:   GH₵ {sum(amounts):.2f}")
        print(f"Mean :   GH₵ {meann:.2f}")
        print(f"Median:  GH₵ {median(amounts):.2f}")
        print(f"SD:      GH₵ {sd:.2f}")
        print(f"Biggest: GH₵ {biggest:.2f}")
        if z > 2:
            print(f"    z = {z:.2f} (unusual!)")
        else:
            print(f"    z = {z:.2f}")
    except ValueError:
        sys.exit(f"Not a number: {i}")




