number = int(input("Enter number: "))

digits = []
is_prime = True

while number > 0:
    digit = number % 10
    digits += [digit]
    number = number // 10

for digit in digits:
    is_prime = True
    for num in range(2, digit):
        if digit % num == 0:
            is_prime = False
            break
    if is_prime:
        break

if is_prime:
    print("Yes")
else:
    print("No")