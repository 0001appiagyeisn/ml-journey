import requests
import sys

req = requests.get("https://open.er-api.com/v6/latest/USD").json()

rate = req["rates"]["GHS"]

if len(sys.argv) == 2:
    print(f"GHC {sys.argv[1]} = ${(float(sys.argv[1]) / rate):.2f}")
elif len(sys.argv) == 1:
    print(f"1 USD = GHC {rate:.2f}")



