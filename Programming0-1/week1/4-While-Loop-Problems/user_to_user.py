a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = a
end = b

if a > b:
    start = b
    end = a
elif a == b:
    print(a)
    exit()

while start <= end:
    print(start)
    start += 1