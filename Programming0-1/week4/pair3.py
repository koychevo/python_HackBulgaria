def is_prime(number):
    for n in range(2, number):
        if number % 2 == 0:
            return False
    return True

def prime_pair(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i, length):
            if is_prime(numbers[i] + numbers[j]):
                return True
    return False

print(prime_pair([1, 2, 3, 5, 7]))
print(prime_pair([2, 6, 10, 4]))
