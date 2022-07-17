n = int(input("Enter n: "))

sum = 0

for number in range(n + 1):
    if number % 2 != 0:
        sum += number

print(sum)