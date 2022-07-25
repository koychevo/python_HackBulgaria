def divisors(n):
    divisors = []
    for number in range(1, n):
        if n % number == 0:
            divisors += [number]
    return divisors

def sum_ints(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

n = int(input("Enter n: "))

print(sum_ints(divisors(n)))
