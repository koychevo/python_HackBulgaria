n = int(input("Enter n: "))

divisors = []

for number in range(1, n):
    if n % number == 0:
        divisors += [number]

for number in divisors:
    print(number)