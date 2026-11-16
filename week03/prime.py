from safe_input import get_int


def is_prime():
    n = get_int("Enter a number: ")
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return print("Not a prime number") #found a divisor
        d += 1
    return print("Prime Number")


