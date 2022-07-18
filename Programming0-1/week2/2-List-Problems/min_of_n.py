n = int(input("Enter n: "))
numbers = []

for i in range(n):
    number = int(input("Enter number: "))
    numbers += [number]

min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number

print(f"Min is: {min_number}")