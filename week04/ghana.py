def main():
    print(cedis(1234.5))
    print(greet("Kwadwo"))

def cedis(amount):
    return f"GH₵ {amount:,.2f}"
def greet(name):
    return f"Akwaaba, {name}!"

if __name__ == "__main__":
    main()