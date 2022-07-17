n = int(input("Enter n: "))
m = int(input("Enter m: "))

if n < m:
    start = n
    end = m
else:
    start = m
    end = n

for number in range(start, end + 1):
    digits_sum = 0
    current_number = number
    while number != 0:
        digits_sum += number % 10
        number //= 10
    print(f"Sum of digits of {current_number} = {digits_sum}")