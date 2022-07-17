n = int(input("Enter number: "))

is_prime = True

for number in range(2, n):
    if n % number == 0:
        is_prime = False
        break

if is_prime:
    print(f"The {n} is prime")
else:
    print(f"The number {n} is not prime")