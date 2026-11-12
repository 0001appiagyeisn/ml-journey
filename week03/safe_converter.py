#asking for user amount using try and except
try:
    amount_cedis = float(input("Enter amount Ghc: "))
except ValueError:
    print("Thats not an amount")
else:
    dollars = amount_cedis / 15.5
    print(f"Ghc {amount_cedis} -> ${dollars:.2f}")