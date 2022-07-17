n = int(input("Enter number: "))

reverse_n = 0
number = n

while number != 0:
    reverse_n = reverse_n * 10 + number % 10
    number //= 10

if n == reverse_n:
    print(f"The number {n} is palindrom")
else:
    print(f"The number {n} is not palindrom")
