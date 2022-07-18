n = int(input("Enter number: "))

number_to_list = []

while n != 0:
    number_to_list = [n % 10] + number_to_list
    n //= 10

print(number_to_list)

number = 0

for digit in number_to_list:
    number = number * 10 + digit

print(number)