n = int(input("Enter n: "))

numbers = []

for i in range(n):
    number = int(input("Enter number: "))
    numbers += [number]

max_number = numbers[0]
index = 1

while index < len(numbers):
    if max_number < numbers[index]:
        max_number = numbers[index]
    index += 1

print(f"Max is: {max_number}")