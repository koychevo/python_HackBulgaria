n = int(input("Enter n: "))

names = []

for i in range(n):
    name = input()
    names += [name]

names.sort()

for name in names:
    print(name)