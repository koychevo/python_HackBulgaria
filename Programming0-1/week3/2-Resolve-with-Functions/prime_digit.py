def is_prime(n):
    prime_digits = [1, 2, 3, 5, 7]
    if n in prime_digits:
        return True
    return False

def to_digits(n):
    items = []
    while n != 0:
        items += [n % 10]
        n //= 10
    return items

def is_prime_digit(digits):
    for digit in digits:
        if is_prime(digit):
            return True
    return False


n = int(input("Enter number: "))

digits = to_digits(n)
if is_prime_digit(digits):
    print("Yes")
else:
    print("No")

