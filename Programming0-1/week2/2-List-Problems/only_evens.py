n = int(input("Enter n: "))

even_count = 0
even_numbers = []

for i in range(n):
    number = int(input("Enter number: "))
    if number % 2 == 0:
        even_count += 1
        even_numbers += [number]

print(f"Count of evens: {even_count}")

if even_count > 0:
    for number in even_numbers:
        print(number)