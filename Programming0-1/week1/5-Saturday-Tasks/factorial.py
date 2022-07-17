n = int(input("Enter number: "))

fact = 1
for number in range(1, n + 1):
    fact *= number

print(f"{n}! = {fact}")