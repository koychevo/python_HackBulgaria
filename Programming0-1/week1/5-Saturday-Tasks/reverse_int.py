n = int(input("Enter number: "))

digits = []
reverse_number = 0
while n != 0:
    #digits += [n % 10]
    digit = n % 10
    reverse_number = reverse_number * 10 + digit
    n //= 10

print(reverse_number)