n = int(input("Enter n: "))

number = 2

while n > 0:
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if sum == number:
        print(number)
        n -= 1
    number += 1
