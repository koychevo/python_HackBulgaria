n = int(input("Enter n: "))

start = 1
numbers = []

while start <= n:
    number = int(input("Enter number"))
    numbers += [number]
    start += 1

sum = 0

for number in numbers:
    sum += number

print(f"Avg is: {sum / n}")