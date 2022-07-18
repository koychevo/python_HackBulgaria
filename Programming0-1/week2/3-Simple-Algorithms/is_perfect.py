n = int(input("Enter number: "))

divisors = []
sum = 0
#is_perfect = True

for number in range(1, n):
    if n % number == 0:
        divisors += [number]

for number in divisors:
    sum += number

if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")