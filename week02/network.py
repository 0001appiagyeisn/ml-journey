number = input("Enter Telephone number: ").strip()

while len(number) != 10:
    number = input("Enter phone number must be 10 digits: ").strip()



match number[0:3]:
    case "024" | "054" | "055" | "059":
        print("MTN")
    case "020" | "050":
        print("Telecel")
    case "026" | "027" | "056" | "057":
        print("AT")
    case _:
        print("Unknown network")