n = int(input("Enter n: "))

for row in range(n // 2 + 1):
    line = "." * row + "*" * (n - 2 * row) + "." * row
    print(line)

for row in range(n // 2):
    line = "." * (n // 2 - 1 - row) + "*" * (n - 2 * (n // 2 - 1 - row)) + "." * (n // 2 - 1 - row)
    print(line)