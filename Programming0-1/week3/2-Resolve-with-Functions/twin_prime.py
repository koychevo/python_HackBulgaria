def is_prime(n):
    for number in range(2, n):
        if n % number == 0:
            return False
    return True




p = int(input("Enter number: "))

if not is_prime(p):
    print(f"{p} is not prime.")
else:
    twins = []
    if is_prime(p - 2):
        twins += [p - 2]
    if is_prime(p + 2):
        twins += [p + 2]

    if len(twins) == 0:
        print(f"{p} is prime but:")
        print(f"{p - 2} is not")
        print(f"{p + 2} is not")
    elif len(twins) == 1:
        print(f"Twin primes with {p}:")
        print(f"{min(twins[0], p)}, {max(twins[0], p)}")
    else:
        print(f"Twin primes with {p}:")
        print(f"{twins[0]}, {p}")
        print(f"{p}, {twins[1]}")
