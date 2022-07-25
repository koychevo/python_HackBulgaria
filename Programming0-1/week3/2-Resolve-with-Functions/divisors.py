def divisors(n):
    divisors = []
    for number in range(1, n):
        if n % number == 0:
            divisors += [number]
    return divisors


n = int(input("Enter n: "))
print(divisors(n))
