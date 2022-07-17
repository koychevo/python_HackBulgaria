n = int(input("Enter n: "))

sum = 0

for number in range(2, n + 1, 2):
    sum += number

print(sum)