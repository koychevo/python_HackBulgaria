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


def is_perfect(n):
    is_number_perfect = False
    sum = sum_ints(divisors(n))
    if sum == n:
        is_number_perfect = True
    return is_number_perfect


n = int(input("Enter n: "))

if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not perfect number")