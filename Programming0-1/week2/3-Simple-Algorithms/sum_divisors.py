n = int(input("Enter n: "))

divisors = []
sum = 0

for number in range(1, n):
    if n % number == 0:
        divisors = divisors + [number]

for number in divisors:
    sum += number

print(f"Sum is: {sum}")