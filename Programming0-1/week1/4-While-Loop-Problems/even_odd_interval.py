a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = a
end = b

if a > b:
    start = b
    end = a

while start <= end:
    number_kind = "odd"
    if start % 2 == 0:
        number_kind = "even"
    print(f"{start} - {number_kind}")
    start += 1