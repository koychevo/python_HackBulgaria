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

def first_n_perfect(n):
    perfect_numbers = []
    number = 1

    while len(perfect_numbers) < n:
        if is_perfect(number):
            perfect_numbers += [number]
        number += 1

    return perfect_numbers

n = int(input("Enter n: "))
perfect_number = first_n_perfect(n)

for number in perfect_number:
    print(number)