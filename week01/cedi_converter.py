#Ask user for amount in cedi
amount_cedi = float(input("Enter Amount in Cedi: "))

#Cedi to dollar converter
converter = amount_cedi * 0.086022

print(f"GHS{amount_cedi} = ${converter:.2f} dollars.")
