n = int(input("Enter number: "))

largest_number = 0
smallest_number = 0
a = n % 10
n = n // 10
b = n % 10
c = n // 10

if a >= b and b >= c:
    largest_number = a * 100 + b * 10 + c
    smallest_number = c * 100 + b * 10 + a
elif a >= c and c >= b:
    largest_number = a * 100 + c * 10 + b
    smallest_number = b * 100 + c * 10 + a
elif b >= a and a >= c:
    largest_number = b * 100 + a * 10 + c
    smallest_number = c * 100 + a * 10 + b
elif b >= c and c >= a:
    largest_number = b * 100 + c * 10 + a
    smallest_number = a * 100 + c * 10 + b
elif c >= a and a >= b:
    largest_number = c * 100 + a * 10 + b
    smallest_number = b * 100 + a * 10 + c
elif c >= b and b >= a:
    largest_number = c * 100 + b * 10 + a
    smallest_number = a * 100 + b * 10 + c


print(largest_number)
print(smallest_number)